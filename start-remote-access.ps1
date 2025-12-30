Write-Host "Starting Pizza Helper Remote Access..."
Write-Host "Forwarding port 3069 to the application..."
Write-Host "You can access the application at: http://<YOUR-PC-IP>:3069"
Write-Host "Press Ctrl+C to stop."

kubectl port-forward --address 0.0.0.0 svc/pizza-helper-frontend 3069:80 -n pizza-helper