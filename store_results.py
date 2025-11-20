from sqlalchemy import create_engine, text
from config import DB_URI
import json


engine = create_engine(DB_URI, pool_pre_ping=True)


INSERT_SQL = '''
INSERT INTO ml (company_id, company_name, pros, cons, metrics, model_output, source_api_response, status)
VALUES (:company_id, :company_name, :pros, :cons, :metrics, :model_output, :source_api_response, :status)
ON DUPLICATE KEY UPDATE
pros = VALUES(pros), cons = VALUES(cons), metrics = VALUES(metrics), model_output = VALUES(model_output), source_api_response = VALUES(source_api_response), status = VALUES(status), analysis_date = CURRENT_TIMESTAMP();
'''




def save_to_db(company_id, company_name, pros, cons, metrics, model_output, raw_response, status='completed'):
    with engine.begin() as conn:
        conn.execute(text(INSERT_SQL), {
        'company_id': company_id,
        'company_name': company_name,
        'pros': json.dumps(pros),
        'cons': json.dumps(cons),
        'metrics': json.dumps(metrics),
        'model_output': json.dumps(model_output),
        'source_api_response': json.dumps(raw_response),
        'status': status