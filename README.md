# Rideau Canal Skateway Monitoring
## Scenario: Rideau Canal Skateway Monitoring

The Rideau Canal Skateway, a historic and world-renowned attraction in Ottawa, needs constant monitoring to ensure skater safety. Your team has been hired by the National Capital Commission (NCC) to build a real-time data streaming system that will:

- Simulate IoT sensors to monitor ice conditions and weather factors along the canal.
- Process incoming sensor data to detect unsafe conditions in real time.
- Store the results in Azure Blob Storage for further analysis.
## Architecture Diagram
```mermaid
graph LR
    subgraph "IoT Sensors"
        S1[Dow's Lake Sensor]
        S2[Fifth Avenue Sensor]
        S3[NAC Sensor]
    end

    subgraph "Azure Cloud"
        IH[Azure IoT Hub]
        ASA[Azure Stream Analytics]
        BS[(Azure Blob Storage)]
    end

    %% Sensor data flow to IoT Hub
    S1 -->|JSON Data| IH
    S2 -->|JSON Data| IH
    S3 -->|JSON Data| IH

    %% IoT Hub to Stream Analytics
    IH -->|Raw Sensor Data| ASA

    %% Stream Analytics processing and storage
    ASA -->|5-min Aggregated Data| BS
```