package com.example.controller;

import cn.dev33.satoken.annotation.SaCheckLogin;
import cn.dev33.satoken.stp.StpUtil;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import com.example.pojo.User;
import com.example.service.UserService;
import com.example.util.Result;
import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController
{
    @Resource
    private UserService userService;

    @PostMapping("/userLogin")
    public Result userLogin(@RequestBody User user)
    {
        String id = user.getUserID();
        User tempUser = userService.getOne(new QueryWrapper<User>().eq("userID", id));
        if (tempUser == null)
        {
            return Result.error("User Not Exist!");
        }
        else
        {
            if (!tempUser.getPassword().equals(user.getPassword()))
            {
                return Result.error("Wrong Password!");
            }
            else
            {
                userService.update(new UpdateWrapper<User>().eq("userID", id).set("login", 1));
                StpUtil.login(id);
                return Result.success("Login Success!", StpUtil.getTokenInfo().getTokenValue());
            }
        }
    }

    @PostMapping("/userRegs")
    public Result userRegs(@RequestBody User user)
    {
        String id = user.getUserID();
        User tempUser = userService.getOne(new QueryWrapper<User>().eq("userID", id));
        if (tempUser != null)
        {
            return Result.error("Already Registered!");
        }
        else
        {
            userService.save(user);
            return Result.success("Register Success");
        }
    }

    @GetMapping("/userLogout")
    @SaCheckLogin
    public Result userLogout()
    {
        String id = StpUtil.getLoginId().toString();
        User tempUser = userService.getOne(new QueryWrapper<User>().eq("userID", id));
        userService.update(new UpdateWrapper<User>().eq("userID", id).set("login", 0));
        StpUtil.logout(id);
        return Result.success("Logout Success");
    }

    @GetMapping("/userInfo")
    @SaCheckLogin
    public Result userInfo()
    {
        String id = StpUtil.getLoginId().toString();
        User tempUser = userService.getOne(new QueryWrapper<User>().eq("userID", id));
        return Result.success("Show Info", tempUser);
    }
}
