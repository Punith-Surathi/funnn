{
  "type": "record",
  "name": "ScoringOutput",
  "namespace": "com.punith.kafka",
  "fields": [
    { "name": "id", "type": "string" },
    { "name": "model_name", "type": "string" },
    { "name": "model_version", "type": "string" },
    { "name": "scored_at", "type": "long" },  // UNIX timestamp
    {
      "name": "result",
      "type": [
        {
          "type": "record",
          "name": "ASubIDGroup",
          "fields": [
            { "name": "scoring_ticket_id", "type": { "type": "enum", "name": "ASubIDs", "symbols": ["a_sub_id2", "a_sub_id5", "a_sub_id10"] } },
            { "name": "pred_class", "type": "string" },
            { "name": "pred_0", "type": "double" },
            { "name": "pred_1", "type": "double" }
          ]
        },
        {
          "type": "record",
          "name": "ASubClsGroup",
          "fields": [
            { "name": "scoring_ticket_id", "type": { "type": "enum", "name": "ASubCls", "symbols": ["a_sub_cls"] } },
            { "name": "pred_class", "type": "string" },
            { "name": "pred_nodemand", "type": "double" },
            { "name": "pred_send_demand", "type": "double" }
          ]
        },
        {
          "type": "record",
          "name": "PSubIDGroup",
          "fields": [
            { "name": "scoring_ticket_id", "type": { "type": "enum", "name": "PSubID", "symbols": ["p_sub_id"] } },
            { "name": "pred_0", "type": "double" },
            { "name": "pred_sub0", "type": "double" },
            { "name": "pred_sub1", "type": "double" }
          ]
        }
      ]
    }
  ]
}
