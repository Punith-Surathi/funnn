{
  "type": "record",
  "name": "UserActivity",
  "namespace": "com.punith.kafka",
  "fields": [
    { "name": "event_id", "type": "string" },
    { "name": "user", "type": "string" },
    { "name": "created_at", "type": "long" },
    {
      "name": "event_details",
      "type": [
        {
          "type": "record",
          "name": "ClickEvent",
          "fields": [
            { "name": "event_type", "type": { "type": "enum", "name": "ClickTypeEnum", "symbols": ["click"] } },
            { "name": "element_id", "type": "string" },
            { "name": "page", "type": "string" }
          ]
        },
        {
          "type": "record",
          "name": "PurchaseEvent",
          "fields": [
            { "name": "event_type", "type": { "type": "enum", "name": "PurchaseTypeEnum", "symbols": ["purchase"] } },
            { "name": "product_id", "type": "string" },
            { "name": "price", "type": "double" },
            { "name": "currency", "type": "string" }
          ]
        }
      ]
    }
  ]
}
