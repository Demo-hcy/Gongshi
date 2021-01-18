if (#ref("$productId.$devId.properties.$property1[0].brightness") > number && #ref("$productId.$devId.properties.$property2") < number)
{
    #call_service("$productId.$devId.services.$service", param1=value1, param2=value2...);
}
else
{
    #raise_event("$eventId",srcList="[{\"productId\": $productId, \"deviceId\": $deviceId}]");
}