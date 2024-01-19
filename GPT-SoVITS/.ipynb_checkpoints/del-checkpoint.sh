#!/bin/bash
cd /root/autodl-tmp/workdir/GPT-SoVITS
rm -rf GPT_weights/*
rm -rf SoVITS_weights/*

rm -rf input/*
rm -rf output/asr_opt/*
rm -rf output/slicer_opt/*
rm -rf output/uvr5_opt/*
rm -rf logs/*

echo 初始化完成