CREATE TABLE product_area (
    id integer NOT NULL auto_increment,
    name nvarchar(500) NOT NULL,
    primary key (id)
);

insert into product_area (name)
values ('Policies'), ('Billing'), ('Claims'), ('Reports');

ALTER TABLE feature_request
  ADD COLUMN product_area_id INTEGER NOT NULL DEFAULT 1,
  ADD CONSTRAINT fk_product_area FOREIGN KEY (product_area_id)
  REFERENCES product_area(id);

