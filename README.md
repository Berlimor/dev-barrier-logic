# dev-barrier-logic

### Deployment
Follow these steps to start the service:
```
git clone https://github.com/Berlimor/dev-barrier-logic.git
cd dev-barrier-logic
docker-compose up --build -d
```
____
### Endpoints

##### /feecc-barrier-logic/stream
SSE stream which returns json data once every 5 seconds.
```json
"data": {
    "license_plate": "A123BC",
    "reason": "Status should be 'Used in 1c', not Weighted."
}
```

##### /feecc-barrier-logic/force-open
Dummy endpoint, returns with status code 200.