def handler(event, context):
    print("Received request with payload", event)
    
    return {"message": "Successfully executed"}
