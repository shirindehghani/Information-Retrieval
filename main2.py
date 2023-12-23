from IR_models.Retrieval import query_builder_andRetrieve

response=query_builder_andRetrieve("mom text", api_key="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")
print(len(response))