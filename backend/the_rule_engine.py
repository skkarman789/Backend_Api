from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Data, AlertThreshold, Alert
from .serializers import AlertSerializer
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

scheduler = BackgroundScheduler()
scheduler.start()

# API endpoint to get details of a specific alert
@api_view(['GET'])
def get_alert(request, alert_id):
    try:
        alert = Alert.objects.get(alert_id=alert_id)
        return Response({'alert_id': alert.alert_id, 'location': alert.location_type, 'timestamp': alert.created_at})
    except Alert.DoesNotExist:
        return Response({'message': 'Alert not found'}, status=404)

# API endpoint to get all alerts within the last 5 minutes
@api_view(['GET'])
def get_all_alerts(request):
    try:
        generate_alerts()
        cutoff_time = timezone.now() - timedelta(minutes=5)
        recent_alerts = Alert.objects.filter(created_at__gte=cutoff_time)
        serialized_data = AlertSerializer(recent_alerts, many=True).data
        return Response({'alerts': serialized_data})
    except Alert.DoesNotExist:
        return Response({'message': 'Alerts not found'}, status=404)

# Function to generate alerts based on certain conditions
def generate_alerts():
    for location, threshold in AlertThreshold.objects.values_list('location_type', 'threshold'):
        event_count = Data.objects.filter(
            location_type=location,
            timestamp__gte=(timezone.now() - timedelta(minutes=5)),
            is_overspeeding=False
        ).count()
        
        overspeeding_condition = Data.objects.filter(location_type=location, is_overspeeding=True).count() >= 1
        # print(f"Location: {location}, Event Count: {event_count}, Overspeeding Condition: {overspeeding_condition}")

        if event_count >= threshold or overspeeding_condition:
            last_alert = Alert.objects.filter(location_type=location).order_by('-created_at').first()

            if last_alert is None:
                Alert.objects.create(location_type=location)
                Data.objects.filter(location_type=location, timestamp__gte=(timezone.now() - timedelta(minutes=5))).delete()
            else:
                time_difference = timezone.now() - last_alert.created_at
                if time_difference >= timedelta(minutes=5):
                    Alert.objects.create(location_type=location)
                    Data.objects.filter(location_type=location, timestamp__gte=(timezone.now() - timedelta(minutes=5))).delete()

# Schedule the job to run every 5 min
scheduler.add_job(generate_alerts, 'interval', minutes=5)
# Shutdown the scheduler on exit
atexit.register(lambda: scheduler.shutdown())
