package com.example.controller;

import com.alibaba.fastjson2.JSON;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.pojo.Environment;
import com.example.pojo.Posture;
import com.example.server.WebServer;
import com.example.service.EnvironmentService;
import com.example.service.PostureService;
import jakarta.annotation.Resource;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

import java.io.IOException;

@EnableScheduling
@Configuration
public class ScheduleController
{
    @Resource
    private EnvironmentService environmentService;
    @Resource
    private PostureService postureService;

    @Scheduled(fixedRate = 5000)
    public void environment() throws IOException
    {
        long envCount = environmentService.count();
        if (envCount > 0)
        {
            Environment env = environmentService.getOne(new QueryWrapper<Environment>().eq("envID", envCount));
            double tempC = env.getTemperature();
            double humid = env.getHumidity();
            double tempF = tempC * 1.8 + 32;
            double rh = humid / 100;
            double apparentTemp = -42.379 + (2.04901523 * tempF) + (10.14333127 * rh) - (0.22475541 * tempF * rh) - (6.83783 / 1000 * tempF * tempF) - (5.481717 / 100 * rh * rh) + (1.22874 / 1000 * tempF * tempF * rh) + (8.5282 / 10000 * tempF * rh * rh) - (1.99 / 1000000 * tempF * tempF * rh * rh);
            apparentTemp = (apparentTemp - 32) / 1.8;
            WebServer.push("1", msg2Json("200", "send temp", tempC));
            WebServer.push("1", msg2Json("200", "send humid", humid));
            System.out.println("Apparent Temp: " + apparentTemp);
            if (apparentTemp >= 32)
            {
                WebServer.push("1", msg2Json("200", "send advice", "It is not suitable for exercise now. Take a rest!"));
            }
            else
            {
                WebServer.push("1", msg2Json("200", "send advice", "It is suitable for exercise now. Come on!"));
            }
        }
    }

    @Scheduled(fixedRate = 1000)
    public void posture() throws IOException
    {
        long posCount = postureService.count();
        if (posCount > 0)
        {
            Posture pos = postureService.getOne(new QueryWrapper<Posture>().eq("posID", posCount));
            WebServer.push("1", msg2Json("200", "send status", pos.getStatus()));
        }
    }

    public static String msg2Json(String httpStatus, String msg, Object data)
    {
        String jsonData = JSON.toJSONString(data);
        return "{\"status\":\"" + httpStatus + "\",\"msg\":\"" + msg + "\",\"data\":" + jsonData + "}";
    }
}
