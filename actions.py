def get_models():
  import sqlmodel as sql
  
  sql_model_subclasses = sql.SQLModel.__subclasses__()
  
  if sql_model_subclasses:
    sql_models = sql_model_subclasses[:]
    
    for sql_model_subclass in sql_model_subclasses:
      sql_models.extend(sql_model_subclass.__subclasses__())
    
    return sql_models
  
  return []