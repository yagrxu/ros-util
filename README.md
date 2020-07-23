# ros-util

## Why

## Current ROS Setup

Template01.json |-> Stack01-----｜
                |-> Stack02     ｜
Template02.json |-> Stack03-----｜
                |-> Stack04     ｜
Template03.json ----------------｜-> Stack05 (it can refer to Stack01 and Stack03)

Template.json -> StackGroup |-> Stack01 (with config01)
                            |-> Stack02 (with config02)
                            |-> Stack02 (with config03)

## What is possible now

Template01.json --|                    |---> Stack01
Template02.json --| --> values.json -->|---> Stack02
Template03.json --|                    |---> Stack03

## What I want to achieve

Be able to re-use the code
Template01.json ---|
Template02.json ---|--->Aggregated Temp Template ---> Stack01 (including 3 templates)
Template03.json ---|

This will also includes the feature of StackGroup
