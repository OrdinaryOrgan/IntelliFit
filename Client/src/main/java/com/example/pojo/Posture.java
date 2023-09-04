package com.example.pojo;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

import java.util.Date;


@TableName("Posture")
public class Posture
{
    @TableId("posID")
    private Integer posID;
    @TableField
    private Integer status;
    private Date date;

    public Integer getPosID()
    {
        return posID;
    }

    public void setPosID(Integer posID)
    {
        this.posID = posID;
    }

    public Integer getStatus()
    {
        return status;
    }

    public void setStatus(Integer status)
    {
        this.status = status;
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
