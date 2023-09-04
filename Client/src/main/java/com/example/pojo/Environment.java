package com.example.pojo;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

import java.util.Date;


@TableName("Environment")
public class Environment
{
    @TableId("envID")
    private Integer envID;
    @TableField
    private Double temperature;
    private Double humidity;
    private Date date;

    public Integer getEnvID()
    {
        return envID;
    }

    public void setEnvID(Integer envID)
    {
        this.envID = envID;
    }

    public Double getTemperature()
    {
        return temperature;
    }

    public void setTemperature(Double temperature)
    {
        this.temperature = temperature;
    }

    public Double getHumidity()
    {
        return humidity;
    }

    public void setHumidity(Double humidity)
    {
        this.humidity = humidity;
    }

    public Date getDate()
    {
        return date;
    }

    public void setDate(Date date)
    {
        this.date = date;
    }
}
