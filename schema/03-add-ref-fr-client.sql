ALTER TABLE feature_request
  ADD COLUMN client_id INTEGER NOT NULL,
  ADD CONSTRAINT fk_client FOREIGN KEY (client_id)
  REFERENCES client(id)
