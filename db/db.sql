
/*BODEGA*/

CREATE TABLE IF NOT EXISTS bodega.producto
(
    id integer NOT NULL DEFAULT nextval('bodega."Producto_id_seq"'::regclass),
    codigo_producto character(30) COLLATE pg_catalog."default" NOT NULL,
    nombre character(10) COLLATE pg_catalog."default" NOT NULL,
    descrpcion character(250) COLLATE pg_catalog."default" NOT NULL,
    precio money NOT NULL,
    CONSTRAINT "Producto_pkey" PRIMARY KEY (id)
);


create table bodega.consola(
 marca character(72) not null,
 modelo character(72) not null)
 /*hereda de producto*/
 inherits ( bodega.producto );


create table bodega.videojuego(
 genero Character(50) not null,
 ano_lanzamiento date not null,
 plataforma Character(72) not null,
 mecanica Character(72) not null)
 inherits (bodega.producto);

/*ejemplo de un insert para consola*/
INSERT INTO bodega.consola (codigo_producto, nombre, descrpcion, precio,categoria ,marca, modelo) VALUES
('C001', 'PlayStation 5', 'Consola de videojuegos PlayStation 5', '499.99',1,'Sony', 'PlayStation 5');

/*ejemplo de un insert para videojuego*/
INSERT INTO bodega.videojuego (codigo_producto, nombre, descrpcion, precio,categoria ,genero, ano_lanzamiento, plataforma, mecanica) VALUES
('V001', 'The Last of Us Part II', 'Juego de acción y aventura', '59.99',2,'Acción', '2020-06-19', 'PlayStation 4', 'Supervivencia');



CREATE TABLE IF NOT EXISTS bodega.bodega
(
    id integer NOT NULL DEFAULT nextval('bodega."Producto_id_seq"'::regclass),
	id_empleado bigint NOT NULL,
    id_sucursal bigint NOT NULL,
    CONSTRAINT "bodega_pkey" PRIMARY KEY (id),
    CONSTRAINT "fk_sucursal" FOREIGN KEY (id_sucursal) REFERENCES sucursal.sucursal(id_sucursal),
	CONSTRAINT  "fk_empleado" FOREIgn key (id_empleado) REFERENCES administrador.empleado(id_empleado)
   
);


CREATE TABLE IF NOT EXISTS bodega.producto_bodega(
 id_producto_bodega serial Not NULL,
 id_bodega BIGINT NOT NULL,
 id_producto BIGINT NOT NULL,
 cantidad int NOT NULL,
 CONSTRAINT "producto_bodega_pkey" PRIMARY KEY (id_producto_bodega),
 CONSTRAINT "fk_producto" FOREIGN KEY (id_producto) REFERENCES bodega.producto(id_producto),
 CONSTRAINT "fk_bodega" FOREIGN KEY (id_bodega) REFERENCES bodega.bodega(id_bodega)
);

/*Administrador*/

CREATE TABLE IF NOT EXISTS administrador.empleado
(
    id_empleado integer NOT NULL DEFAULT nextval('administrador.empleado_id_empleado_seq'::regclass),
    rol char,
	usuario Character(75) UNIQUE NOT NULL ,
	contrasena password NOT NULL,
	id_sucursal bigint NOT NULL,
	nombre Character(75) NOt NULL,
	telefono numeric(8) NOT  NULL,
	correo Character(20) NOT NULL,
	CHECK (correo ~'@'),
	CONSTRAINT empleado_pkey PRIMARY KEY (id_empleado)
)



/*SUCURSAL*/
CREATE TABLE IF NOT EXISTS sucursal.sucursal
(   
    id_sucursal integer NOT NULL DEFAULT nextval('sucursal.sucursal_id_sucursal_seq'::regclass),
    direccion character(150) COLLATE pg_catalog."default" NOT NULL,
    nombre character(72) COLLATE pg_catalog."default" NOT NULL,
    no_sucursal integer NOT NULL,
    CONSTRAINT sucursal_pkey PRIMARY KEY (id_sucursal)
)

/*INVENTARIO*/

CREATE TABLE inventario.estanteria(
	id_estanteria serial NOT NULL,
	id_sucursal integer NOT NULL,
	id_empleado integer NOT NULL,
	CONSTRAINT estateria_pkey PRIMARY KEY (id_estanteria),
	CONSTRAINT "fk_sucursal" FOREIGN KEY (id_sucursal) REFERENCES sucursal.sucursal(id_sucursal),
	CONSTRAINT "fk_empleado" FOREIGN KEY (id_empleado) REFERENCES bodega.bodega(id)
	
);


CREATE TABLE inventario.estanteria_producto(
	id_estanteria_producto serial Not NULL,
	id_estanteria integer NOT NULL,
	id_producto_bodega integer NOT NULL,
	no_pasillo Character(50),
	CONSTRAINT estateria_producto_pkey PRIMARY KEY (id_estanteria_producto),
	CONSTRAINT "fk_estanteria" FOREIGN KEY (id_estanteria) REFERENCES inventario.estanteria(id_estanteria),
	CONSTRAINT "fk_producto_bodega" FOREIGN KEY (id_producto_bodega) REFERENCES bodega.producto_bodega(id_producto_bodega)
);


 /* procedimiento para ingresar un usuario*/
CREATE OR REPLACE PROCEDURE administrador.registrar_empleado(
    rol VARCHAR(10),
    usuario VARCHAR(75),
    contrasena TEXT,
    id_sucursal BIGINT,
    nombre VARCHAR(75),
    telefono NUMERIC(8),
    correo VARCHAR(20),
    no_caja INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF no_caja IS NULL THEN
        -- si el numero de caja es nulo se inserta en empleado   
		 INSERT INTO administrador.empleado (rol, usuario, contrasena, id_sucursal, nombre, telefono, correo)
        VALUES (rol, usuario, contrasena, id_sucursal, nombre, telefono, correo);
		
    ELSE
        INSERT INTO administrador.cajero (rol, usuario, contrasena, id_sucursal, nombre, telefono, correo,no_caja)
        VALUES (rol, usuario, contrasena, id_sucursal, nombre, telefono, correo,no_caja);
    END IF;
END;
$$;


/*inserte de un empleado*/
CALL  administrador.registrar_empleado(
'B','LuisBodega1','123456',1,'Gerardo',77668945,'luis@gmail.com',null);


/*inserte de un cajero*/
CALL  administrador.registrar_empleado('C','Cajero1','123456',1,'cajero',77668945,'cajero@gmail.com',1);

/* Funcion  login  */

CREATE OR REPLACE FUNCTION administrador.login(p_correo VARCHAR(256), p_contrasena TEXT)
RETURNS TABLE(id_empleado BIGINT, id_sucursal BIGINT, rol CHAR, dato BIGINT,nombre character(72)) AS $$
DECLARE
    rol_empleado CHAR;
	idEmpleado BIGINT;
BEGIN
    -- Obtener el rol del empleado basado en correo y contraseña
    SELECT e.rol, e.id_empleado INTO rol_empleado, idEmpleado
    FROM administrador.empleado e
    WHERE e.correo = p_correo AND e.contrasena = p_contrasena;

    -- Verificar el rol y retornar datos diferentes según el rol
    IF rol_empleado = 'B' THEN
        RETURN QUERY
         SELECT e.id_empleado, b.id_sucursal, e.rol, b.id_bodega, s.nombre
        FROM bodega.bodega b
        LEFT JOIN administrador.empleado e ON e.id_sucursal = b.id_sucursal
		INNER JOIN sucursal.sucursal s ON s.id_sucursal = b.id_sucursal WHERE e.id_empleado=idEmpleado;

    ELSIF rol_empleado = 'I' THEN
        RETURN QUERY
        SELECT   e.id_empleado, i.id_sucursal, e.rol,  i.id_estanteria, s.nombre 
        FROM inventario.estanteria i
        LEFT JOIN administrador.empleado e ON e.id_sucursal = i.id_sucursal
		INNER JOIN sucursal.sucursal s ON s.id_sucursal = i.id_sucursal WHERE e.id_empleado=idEmpleado;

    ELSIF rol_empleado = 'C' THEN
        RETURN QUERY
        SELECT c.id_empleado, c.id_sucursal, c.rol, c.no_caja, s.nombre
        FROM administrador.cajero c
		INNER  JOIN sucursal.sucursal s ON s.id_sucursal = c.id_sucursal WHERE  c.id_empleado=idEmpleado;

    ELSIF rol_empleado = 'A' THEN
        RETURN QUERY
       	SELECT a.id_empleado, a.id_sucursal, a.rol,NULL::BIGINT, s.nombre
        FROM administrador.empleado a
		INNER JOIN sucursal.sucursal s ON s.id_sucursal = a.id_sucursal  WHERE a.id_empleado=idEmpleado;

    ELSE
        RETURN QUERY
        SELECT NULL::BIGINT AS id_empleado, NULL::BIGINT AS id_sucursal, NULL::BIGINT AS rol, 'Rol desconocido' AS datos ,NULL::VARCHAR(75);
    END IF;
END;
$$ LANGUAGE plpgsql;




 CREATE OR REPLACE PROCEDURE bodega.obtener_producto(p_id_producto BIGINT)
LANGUAGE plpgsql
AS $$
DECLARE
    categoria integer;
	v_result RECORD;
BEGIN 

	SELECT p.categoria INTO categoria
    FROM bodega.producto p
    WHERE p.id_producto = p_id_producto; 

 IF categoria = 1 THEN
        -- Consultar y devolver información de consola
        FOR v_result IN
            SELECT * FROM bodega.consola
            WHERE id_producto = p_id_producto
        LOOP
            RAISE NOTICE 'Consola: %', v_result;
        END LOOP;
    ELSE
        
        FOR v_result IN
            SELECT * FROM bodega.videojuego
            WHERE id_producto = p_id_producto
        LOOP
            RAISE NOTICE 'Videojuego: %', v_result;
        END LOOP;
    END IF;
END;
$$;

/*funcion para insertar y retornar id */

CREATE OR REPLACE FUNCTION sucursal.inser_sucursal(
    p_direccion varchar(150),
    p_nombre varchar(72),
    p_no_sucursal integer,
    p_codigo varchar(72),
    p_correo varchar(150),
    p_telefono varchar(20), 
    p_horario_apertura time,
    p_horario_cierre time
)
RETURNS INTEGER AS $$
DECLARE
    id INTEGER;
BEGIN
    INSERT INTO sucursal.sucursal (
        direccion, nombre, no_sucursal, codigo, correo, telefono, horario_apertura, horario_cierre
    )
    VALUES (
        p_direccion, 
        p_nombre,
        p_no_sucursal,
        p_codigo,
        p_correo,
        p_telefono,
        p_horario_apertura,
        p_horario_cierre
    )
    RETURNING id_sucursal INTO id; 
    RETURN id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE  sucursal.insert_sucursal(
    p_direccion VARCHAR(150),
    p_nombre VARCHAR(72),
    p_no_sucursal INTEGER,
    p_codigo VARCHAR(72),
    p_correo VARCHAR(150),
    p_telefono VARCHAR(20),
    p_horario_apertura TIME,
    p_horario_cierre TIME,
    OUT p_id_sucursal INTEGER  
)
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO sucursal.sucursal (
        direccion, nombre, no_sucursal, codigo, correo, telefono, horario_apertura, horario_cierre
    )
    VALUES (
        p_direccion, 
        p_nombre,
        p_no_sucursal,
        p_codigo,
        p_correo,
        p_telefono,
        p_horario_apertura,
        p_horario_cierre
    )
    RETURNING id_sucursal INTO p_id_sucursal; 
	
	INSERT INTO bodega.bodega(id_empleado, id_sucursal)
	VALUES (null,id_sucursal  );

	INSERT INTO administrador.admin(id_empleado, id_sucursal)
	VALUES (null,id_sucursal  );

	INSERT INTO cajero.caja(id_empleado, id_sucursal)
	VALUES (null,id_sucursal  );

	INSERT INTO inventario.estanteria(id_empleado, id_sucursal)
	VALUES (null,id_sucursal  );
	
END;
$$;

/*metodo para insertar  productos a la bodega*/
CREATE PROCEDURE bodega.inser_producto_bodega(p_id_bodega BIGINT, p_id_producto BIGINT, p_cantidad BIGINT)
LANGUAGE plpgsql
AS $$
DECLARE 
    idProducto BIGINT;
BEGIN 
    -- Selecciona el id_producto
    SELECT id_producto INTO idProducto 
    FROM bodega.producto_bodega 
    WHERE id_bodega = p_id_bodega AND id_producto = p_id_producto;

    IF idProducto IS NULL THEN
        -- Si no existe, inserta el nuevo producto
        INSERT INTO bodega.producto_bodega (id_bodega, id_producto, cantidad)
        VALUES (p_id_bodega, p_id_producto, p_cantidad);
    ELSE
        -- Si existe, actualiza la cantidad
        UPDATE bodega.producto_bodega
        SET cantidad = cantidad + p_cantidad
        WHERE id_bodega = p_id_bodega AND id_producto = p_id_producto;
    END IF;
END $$;


/*vista para ver los productos de estanteria */
CREATE OR REPLACE VIEW inventario.productos_estanteria AS
select ep.*, p.*, ip.numero, ip.descripcion as descripcion_pasillo from inventario.estanteria_producto ep
INNER JOIN bodega.producto_bodega pb ON pb.id_producto_bodega= ep.id_producto_bodega
INNER JOIN bodega.producto p ON p.id_producto= pb.id_producto
INNER JOIN inventario.pasillo ip ON ip.id_pasillo= ep.id_pasillo


/*pasillo*/
CREATE TABLE inventario.pasillos (
    id_pasillo SERIAL PRIMARY KEY,
    numero bigint NOT NULL,
    id_sucursal bigint REFERENCES sucursal.sucursal(id_sucursal) ON DELETE CASCADE,
    Descripcion CHARACTER(150)
);

ALTER TABLE inventario.estanteria_producto
ADD CONSTRAINT unique_estanteria_producto UNIQUE (id_estanteria, id_producto_bodega);

/*mover producto de bodega a inventario*/
CREATE OR REPLACE FUNCTION inventario.comprobarexistencia()
RETURNS TRIGGER AS $$
DECLARE ex INTEGER;
BEGIN
  SELECT cantidad  INTO ex FROM bodega.producto_bodega WHERE id_producto = NEW.id_producto;
  IF NEW.cantidad>ex THEN 
    RAISE EXCEPTION 'cantidad insuficiente, actualmente solo hay %',ex;
  END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

/*antes del insert*/
CREATE TRIGGER trigger_comprobar
BEFORE INSERT ON inventario.estanteria_producto
FOR EACH ROW
EXECUTE FUNCTION inventario.comprobarexistencia();


CREATE OR REPLACE FUNCTION inventario.actualizar_bodega()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE bodega.producto_bodega 
  SET cantidad = cantidad - NEW.cantidad
  WHERE id_producto = NEW.id_producto;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

/*despues del insert*/
CREATE TRIGGER trigger_actualizar
AFTER INSERT ON inventario.estanteria_producto
FOR EACH ROW
EXECUTE FUNCTION inventario.actualizar_bodega();


/*actualizar producto de bodega cuando ya existe*/

CREATE OR REPLACE FUNCTION inventario.actualizar_bodega_actualizacion()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE bodega.producto_bodega 
    SET cantidad = cantidad - (NEW.cantidad - OLD.cantidad)
    WHERE id_producto = NEW.id_producto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

/*despues del update*/
CREATE TRIGGER trigger_actualizar_bodega_actualizacion
AFTER UPDATE ON inventario.estanteria_producto
FOR EACH ROW
EXECUTE FUNCTION inventario.actualizar_bodega_actualizacion();


/*proceso para insertar producto de bodega a estanteria*/
CREATE OR REPLACE PROCEDURE inventario.insertar_productos_estanteria(
    p_id_estanteria BIGINT, 
    p_id_producto BIGINT, 
    p_cantidad INTEGER,
    p_id_pasillo BIGINT
)
LANGUAGE plpgsql
AS $$
DECLARE
    id_producto_estanteria BIGINT;
BEGIN

    INSERT INTO inventario.estanteria_producto (id_estanteria, id_producto, cantidad)
    VALUES (p_id_estanteria, p_id_producto, p_cantidad)
    ON CONFLICT (id_producto, id_estanteria)
    DO UPDATE SET cantidad = inventario.estanteria_producto.cantidad + EXCLUDED.cantidad
    RETURNING id_estanteria_producto INTO id_producto_estanteria;

    BEGIN
        INSERT INTO inventario.producto_pasillo (id_estanteria_producto, id_pasillo)
        VALUES (id_producto_estanteria, p_id_pasillo);
    EXCEPTION
        WHEN unique_violation THEN
            RAISE NOTICE 'El producto ya existe en el pasillo: %', p_id_pasillo;
        WHEN OTHERS THEN
            RAISE NOTICE 'Ocurrió un error inesperado: %', SQLERRM;
            
    END;
END;
$$;

/*Producto estanteria */
CREATE VIEW inventario.producto_estanteria as
SELECT 
    ip.id_estanteria, bp.*,ip.cantidad,   
    ARRAY_AGG(p.numero) AS numeros_pasillo,
    ARRAY_AGG(p.descripcion) AS descripciones_pasillo,e.id_sucursal
FROM 
    inventario.estanteria_producto ip
INNER JOIN 
    bodega.producto bp ON bp.id_producto = ip.id_producto
INNER JOIN 
    inventario.producto_pasillo pp ON pp.id_estanteria_producto = ip.id_estanteria_producto
INNER JOIN 
    inventario.pasillo p ON p.id_pasillo = pp.id_pasillo
INNER JOIN inventario.estanteria e ON e.id_estanteria = ip.id_estanteria	
GROUP BY 
    bp.id_producto, ip.cantidad, ip.id_estanteria, e.id_sucursal;  

CREATE TABLE cajero.cliente (
    id_cliente SERIAL  PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nit VARCHAR(9)  NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(200) NOT NULL
)

CREATE TABLE cajero.factura (
    factura_id SERIAL PRIMARY KEY,
    numero_factura VARCHAR(50) UNIQUE NOT NULL,
    fecha_emision DATE NOT NULL,
	id_sucursal  bigint not null,
	id_cajero bigint not null,
	id_cliente  bigint not null,
	total money not null,
	descuento_aplicado  money null

);


create table cajero.detalle_factura(
	id_factura bigint not null,
	id_producto bigint not null,
	cantidad bigint not null
	
);


CREATE TABLE IF NOT EXISTS cajero.factura
(
    factura_id BIGINT SERIAL,
    numero_factura character varying(50) COLLATE pg_catalog."default" NOT NULL,
    fecha_emision date NOT NULL DEFAULT CURRENT_DATE,
    id_sucursal bigint NOT NULL,
    id_cajero bigint NOT NULL,
    id_cliente bigint NOT NULL,
    total money NOT NULL,
    descuento_aplicado money,
    CONSTRAINT factura_pkey PRIMARY KEY (factura_id),
    CONSTRAINT factura_numero_factura_key UNIQUE (numero_factura)
);



CREATE OR REPLACE FUNCTION cajero.generar_numero_factura()
RETURNS TRIGGER AS $$
BEGIN
    NEW.numero_factura := 'FAC-' || nextval('cajero.factura_numero_seq');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE SEQUENCE cajero.factura_numero_seq;

CREATE TRIGGER trigger_numero_factura
BEFORE INSERT ON cajero.factura
FOR EACH ROW
EXECUTE FUNCTION cajero.generar_numero_factura();

/*actualizar estanteria*/



CREATE OR REPLACE FUNCTION cajero.actualizar_inventario()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE inventario.estanteria_producto  
  SET cantidad = cantidad - NEW.cantidad
  WHERE id_producto = NEW.id_producto 
    AND id_estanteria = (SELECT id_estanteria 
                         FROM inventario.estanteria 
                         WHERE id_sucursal = 
						 (select id_sucursal from cajero.factura where  id_factura=NEW.id_factura)
                         LIMIT 1); 
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;



/*despues del insert*/
CREATE TRIGGER trigger_actualizar
AFTER INSERT ON cajero.detalle_factura
FOR EACH ROW
EXECUTE FUNCTION cajero.actualizar_inventario();


CREATE TABLE cajero.tarjeta (
    id_tarjeta SERIAL PRIMARY KEY,
    id_cliente serial  not null,
    tipo_tarjeta VARCHAR(20) NOT NULL CHECK (tipo_tarjeta IN ('Común', 'Oro', 'Platino', 'Diamante')),
    puntos INT DEFAULT 0,
    fecha_emision date NOT NULL DEFAULT CURRENT_DATE
);


/*top 2 de sucursales */

CREATE OR REPLACE VIEW administrador.top_sucursales_ingreso AS
SELECT  ss.nombre, ss.direccion,  horario_apertura, horario_cierre, SUM(total) AS total_ingresado  FROM  cajero.factura cf
INNER JOIN sucursal.sucursal ss ON ss.id_sucursal= cf.id_sucursal
GROUP BY  ss.nombre, ss.direccion, horario_apertura, horario_cierre
ORDER BY  total_ingresado DESC LIMIT 2;




/*top 10 ventas mas grandes */

SELECT * FROM cajero.factura
WHERE  fecha_emision BETWEEN '2023-01-01' AND '2023-12-31'  
ORDER BY  total DESC
LIMIT 10;



/*top 10 articulos mas vendidos*/
CREATE OR REPLACE VIEW administrador.top_articulos_vendidos AS
SELECT  bp.nombre,  SUM(cf.cantidad) AS total_vendido
FROM  cajero.detalle_factura cf
INNER JOIN  bodega.producto bp ON bp.id_producto = cf.id_producto
GROUP BY  bp.id_producto 
ORDER BY  total_vendido DESC
LIMIT 10;



/*top 10 cliente que mas dinero han gastado*/

CREATE OR REPLACE VIEW administrador.top_clientes_gastadores AS
SELECT cc.*, SUM(cf.total) AS total_gastado
FROM cajero.factura cf 
INNER JOIN cajero.cliente cc ON cc.id_cliente = cf.id_cliente
WHERE cc.id_cliente NOT IN (5, 6)  /* Excluye los clientes con id 5 y 6*/
GROUP BY cc.id_cliente
ORDER BY total_gastado DESC
LIMIT 10;


CREATE VIEW administrador.ventas_grandes as 
SELECT cf.numero_factura, ss.nombre as sucursal, cc.nit, cc.nombre as cliente,  cf.fecha_emision, cf.total  FROM cajero.factura cf
INNER JOIN sucursal.sucursal ss ON ss.id_sucursal=cf.id_sucursal
INNER JOIN cajero.cliente cc ON cc.id_cliente = cf.id_cliente


SELECT * FROM administrador.ventas_grandes
                WHERE fecha_emision BETWEEN '2023-01-01'  AND  '2024-12-31'     AND nit NOT IN ('CF', 'cf')
                ORDER BY total DESC
                LIMIT 10




/*historial*/
CREATE TABLE administrador.historial_descuentos (
    id_descuento SERIAL PRIMARY KEY,
    id_factura BIGINT NOT NULL,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    monto MONEY NOT NULL,
    FOREIGN KEY (id_factura) REFERENCES cajero.factura(id_factura)
);

CREATE OR REPLACE FUNCTION administrador.agregar_historial_descuento()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.descuento_aplicado > 0 THEN
        INSERT INTO administrador.historial_descuentos (id_factura, fecha, monto)
        VALUES (NEW.factura_id, CURRENT_DATE, NEW.descuento_aplicado);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_descuento
AFTER INSERT ON cajero.factura
FOR EACH ROW
WHEN (NEW.descuento_aplicado::numeric > 0)
EXECUTE FUNCTION administrador.agregar_historial_descuento();


	