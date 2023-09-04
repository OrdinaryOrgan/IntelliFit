package com.example.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.mapper.PostureMapper;
import com.example.pojo.Posture;
import com.example.service.PostureService;
import org.springframework.stereotype.Service;

@Service
public class PostureServiceImpl extends ServiceImpl<PostureMapper, Posture> implements PostureService
{
}
