#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22

const char* WIFI_SSID = "Wokwi-GUEST";
const char* WIFI_PASSWORD = "";
const char* API_URL = "https://TU-API/mediciones";

const char* DEVICE_ID = "sensor_001";
const char* UBICACION = "Quevedo, Ecuador";

DHT dht(DHTPIN, DHTTYPE);

void enviarMedicion(const char* variable, float valor, const char* unidad) {
  if (WiFi.status() != WL_CONNECTED) return;

  HTTPClient http;
  http.begin(API_URL);
  http.addHeader("Content-Type", "application/json");

  String json = "{";
  json += "\"device_id\":\"" + String(DEVICE_ID) + "\",";
  json += "\"tipo_variable\":\"" + String(variable) + "\",";
  json += "\"valor\":" + String(valor, 2) + ",";
  json += "\"unidad\":\"" + String(unidad) + "\",";
  json += "\"ubicacion\":\"" + String(UBICACION) + "\"";
  json += "}";

  int httpCode = http.POST(json);
  Serial.print(variable);
  Serial.print(" -> HTTP ");
  Serial.println(httpCode);
  Serial.println(http.getString());
  http.end();
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Conectando a WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi conectado");
  Serial.println(WiFi.localIP());
}

void loop() {
  float temperatura = dht.readTemperature();
  float humedad = dht.readHumidity();

  if (isnan(temperatura) || isnan(humedad)) {
    Serial.println("Error leyendo DHT22");
    delay(5000);
    return;
  }

  enviarMedicion("temperatura", temperatura, "C");
  enviarMedicion("humedad", humedad, "%");

  delay(10000);
}