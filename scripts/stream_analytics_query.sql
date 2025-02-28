SELECT
    System.Timestamp AS EventTime,
    deviceId,
    temperature,
    humidity,
    pressure
INTO
    [ADXOutput]
FROM
    [EventHubInput]