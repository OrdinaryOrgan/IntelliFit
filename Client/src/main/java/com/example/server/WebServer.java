package com.example.server;

import jakarta.websocket.*;
import jakarta.websocket.server.PathParam;
import jakarta.websocket.server.ServerEndpoint;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.concurrent.CopyOnWriteArrayList;


@Component
@ServerEndpoint("/conn/{uid}")
public class WebServer
{
    private static Integer userCount = 0;
    private static CopyOnWriteArrayList<WebServer> servers = new CopyOnWriteArrayList<>();
    private Session session;
    private String uid;

    @OnOpen
    public void onOpen(@PathParam("uid") String uid, Session session) throws IOException
    {
        this.session = session;
        this.uid = uid;
        servers.add(this);
        countAsc();
        System.out.println("---Open---");
        System.out.println("New connection: " + uid);
        System.out.println("Online user count: " + getCount());
        System.out.println("----------");
        sendMsg("{\"msg\":\"Connection Success\"}");
    }

    @OnMessage
    public void onMsg(String msg) throws IOException
    {
        System.out.println("---Msg----");
        System.out.println("Receive msg: " + msg);
        System.out.println("From uid: " + uid);
        System.out.println("----------");
        for (WebServer server : servers)
        {
            server.sendMsg(msg);
        }
    }

    @OnClose
    public void onClose()
    {
        servers.remove(this);
        countDesc();
        System.out.println("--Close---");
        System.out.println("Connection close " + this.uid);
        System.out.println("Online user count: " + getCount());
        System.out.println("----------");
    }

    @OnError
    public void onError(Throwable error)
    {
        System.out.println("--Error---");
        error.printStackTrace();
        System.out.println("----------");
    }

    public static synchronized int getCount()
    {
        return userCount;
    }

    public static synchronized void countAsc()
    {
        userCount++;
    }

    public static synchronized void countDesc()
    {
        userCount--;
    }

    public void sendMsg(String msg) throws IOException
    {
        this.session.getBasicRemote().sendText(msg);
    }

    public static void push(@PathParam("uid") String uid, String msg) throws IOException
    {
        System.out.println("---Push---");
        System.out.println("Push to user: " + uid);
        System.out.println("Push msg: " + msg);
        System.out.println("----------");
        for (WebServer server : servers)
        {
            if (server.uid.equals(uid))
            {
                server.sendMsg(msg);
            }
        }
    }
}
