from IR_models.Retrieval import query_builder_andRetrieve

response=query_builder_andRetrieve("mom text", api_key="")
print(len(response))