CREATE TABLE feature_request (
    id integer NOT NULL auto_increment,
    title nvarchar(500) NOT NULL,
    description nvarchar(5000) NOT NULL,
    target_date date NOT NULL,
    primary key (id)
);
    
