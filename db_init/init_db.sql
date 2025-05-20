-- Creación de tablas con control para no crear si ya existen

CREATE TABLE IF NOT EXISTS Finca (
    Id_Finca SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Ubicacion VARCHAR(100),
    Area_Total NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS TipoCultivo (
    Id_TipoCultivo SERIAL PRIMARY KEY,
    Nombre_Tipo VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Cultivo (
    Id_Cultivo SERIAL PRIMARY KEY,
    Id_TipoCultivo INT NOT NULL,
    Variedad VARCHAR(100),
    Fecha_Siembra DATE,
    Id_Finca INT NOT NULL
);

-- Agregar las claves foráneas a Cultivo solo si no existen
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'cultivo_id_finca_fkey' AND table_name='cultivo'
    ) THEN
        ALTER TABLE Cultivo
        ADD CONSTRAINT cultivo_id_finca_fkey FOREIGN KEY (Id_Finca) REFERENCES Finca(Id_Finca) ON DELETE CASCADE;
    END IF;
    
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'cultivo_id_tipocultivo_fkey' AND table_name='cultivo'
    ) THEN
        ALTER TABLE Cultivo
        ADD CONSTRAINT cultivo_id_tipocultivo_fkey FOREIGN KEY (Id_TipoCultivo) REFERENCES TipoCultivo(Id_TipoCultivo) ON DELETE RESTRICT;
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS Cosecha (
    Id_Cosecha SERIAL PRIMARY KEY,
    Fecha_Cosecha DATE NOT NULL,
    Peso NUMERIC(10,2) NOT NULL,
    Precio NUMERIC(10,2) NOT NULL,
    Id_Cultivo INT NOT NULL
);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'cosecha_id_cultivo_fkey' AND table_name='cosecha'
    ) THEN
        ALTER TABLE Cosecha
        ADD CONSTRAINT cosecha_id_cultivo_fkey FOREIGN KEY (Id_Cultivo) REFERENCES Cultivo(Id_Cultivo) ON DELETE CASCADE;
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS Venta (
    Id_Venta SERIAL PRIMARY KEY,
    Fecha_Venta DATE NOT NULL,
    Peso_Vendido NUMERIC(10,2) NOT NULL,
    Id_Cosecha INT NOT NULL
);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'venta_id_cosecha_fkey' AND table_name='venta'
    ) THEN
        ALTER TABLE Venta
        ADD CONSTRAINT venta_id_cosecha_fkey FOREIGN KEY (Id_Cosecha) REFERENCES Cosecha(Id_Cosecha) ON DELETE CASCADE;
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS Rol (
    Id_Rol SERIAL PRIMARY KEY,
    Nombre_Rol VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Usuario (
    Id_Usuario SERIAL PRIMARY KEY,
    Nombre_Usuario VARCHAR(100) NOT NULL UNIQUE,
    Contrasena VARCHAR(255) NOT NULL,
    Id_Rol INT NOT NULL
);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'usuario_id_rol_fkey' AND table_name='usuario'
    ) THEN
        ALTER TABLE Usuario
        ADD CONSTRAINT usuario_id_rol_fkey FOREIGN KEY (Id_Rol) REFERENCES Rol(Id_Rol) ON DELETE RESTRICT;
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS ActividadDiaria (
    Id_Actividad SERIAL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Descripcion TEXT,
    Id_Usuario INT NOT NULL,
    Id_Cultivo INT
);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'actividaddiaria_id_usuario_fkey' AND table_name='actividaddiaria'
    ) THEN
        ALTER TABLE ActividadDiaria
        ADD CONSTRAINT actividaddiaria_id_usuario_fkey FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario) ON DELETE CASCADE;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'actividaddiaria_id_cultivo_fkey' AND table_name='actividaddiaria'
    ) THEN
        ALTER TABLE ActividadDiaria
        ADD CONSTRAINT actividaddiaria_id_cultivo_fkey FOREIGN KEY (Id_Cultivo) REFERENCES Cultivo(Id_Cultivo) ON DELETE SET NULL;
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS LogMantenimiento (
    Id_Log SERIAL PRIMARY KEY,
    Tabla_Afectada VARCHAR(100),
    Accion VARCHAR(50),
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Id_Usuario INT
);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'logmantenimiento_id_usuario_fkey' AND table_name='logmantenimiento'
    ) THEN
        ALTER TABLE LogMantenimiento
        ADD CONSTRAINT logmantenimiento_id_usuario_fkey FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario) ON DELETE SET NULL;
    END IF;
END $$;

-- Índices recomendados para optimizar consultas

CREATE INDEX IF NOT EXISTS idx_cosecha_idcultivo ON Cosecha(Id_Cultivo);
CREATE INDEX IF NOT EXISTS idx_venta_idcosecha ON Venta(Id_Cosecha);
CREATE INDEX IF NOT EXISTS idx_cosecha_fechacosecha ON Cosecha(Fecha_Cosecha);
CREATE INDEX IF NOT EXISTS idx_venta_fechaventa ON Venta(Fecha_Venta);

-- Crear roles de base de datos (roles de acceso a nivel DB)
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'gerente_finca') THEN
        CREATE ROLE gerente_finca LOGIN PASSWORD 'gerente_pass';
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'trabajador_campo') THEN
        CREATE ROLE trabajador_campo LOGIN PASSWORD 'trabajador_pass';
    END IF;
END $$;