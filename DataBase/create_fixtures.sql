CREATE TABLE IF NOT EXISTS service (
service_id UUID PRIMARY KEY not null,
service_name TEXT);

CREATE TABLE IF NOT EXISTS logs (
logs_id UUID PRIMARY KEY not null,
logs_service_id UUID NOT NULL,
logs_time timestamp with time zone,
logs_text jsonb,
logs_ip inet,
foreign key (logs_service_id) references service(service_id));

CREATE INDEX IF NOT EXISTS "IDX_logs_service_id" ON "logs" ("logs_service_id");
CREATE INDEX IF NOT EXISTS "IDX_logs_text" ON "logs" ("logs_text");