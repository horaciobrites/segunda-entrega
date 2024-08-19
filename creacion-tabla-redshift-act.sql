create table horacio_brites0709_coderhouse.datos_macroeconomicos (
	idVariable integer not null,
	cdSerie	integer,
	descripcion varchar(200),
	fecha date,
	valor float,
	Load_date timestamp default current_timestamp,
	Update_date timestamp default current_timestamp,
	primary key (fecha, idvariable)
)
sortkey (fecha);