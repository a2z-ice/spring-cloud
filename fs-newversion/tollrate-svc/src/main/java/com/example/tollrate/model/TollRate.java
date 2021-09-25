package com.example.tollrate.model;


import java.math.BigDecimal;

public class TollRate {

    private int stationId;
    private BigDecimal currentRate;
    private String timestamp;
    private int servicePort;

    public TollRate() {}

    public TollRate(int stationId, BigDecimal currentRate, String timestamp, int servicePort) {
        this.stationId = stationId;
        this.currentRate = currentRate;
        this.timestamp = timestamp;
        this.servicePort = servicePort;
    }

    public int getStationId() {
        return stationId;
    }

    public void setStationId(int stationId) {
        this.stationId = stationId;
    }

    public BigDecimal getCurrentRate() {
        return currentRate;
    }

    public void setCurrentRate(BigDecimal currentRate) {
        this.currentRate = currentRate;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public int getServicePort(){return this.servicePort;}
}