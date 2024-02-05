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

##### /stream
SSE stream which returns json data once every 5 seconds.
```json
{
    "license_plate": "A123BC",
    "reason": "Status should be 'Used in 1c', not Weighted."
}
```