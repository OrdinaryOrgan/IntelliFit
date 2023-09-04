package com.example.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.mapper.EnvironmentMapper;
import com.example.pojo.Environment;
import com.example.service.EnvironmentService;
import org.springframework.stereotype.Service;

@Service
public class EnvironmentServiceImpl extends ServiceImpl<EnvironmentMapper, Environment> implements EnvironmentService
{
}
