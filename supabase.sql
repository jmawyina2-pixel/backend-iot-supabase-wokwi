create table if not exists public.dispositivos (
  device_id text primary key,
  nombre text not null,
  ubicacion text,
  creado_en timestamptz default now()
);

create table if not exists public.mediciones (
  id bigint generated always as identity primary key,
  device_id text not null references public.dispositivos(device_id),
  tipo_variable text not null,
  valor numeric not null,
  unidad text not null,
  timestamp timestamptz not null default now()
);

insert into public.dispositivos (device_id, nombre, ubicacion)
values ('sensor_001', 'ESP32 DHT22', 'Quevedo, Ecuador')
on conflict (device_id) do nothing;

select * from public.mediciones
order by timestamp desc
limit 50;