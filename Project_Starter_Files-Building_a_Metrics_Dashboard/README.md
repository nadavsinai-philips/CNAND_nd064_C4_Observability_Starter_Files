**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

TASK1 - DONE - run `kubectl` command to show the running pods and services for all components.  - screenshots available (task 1 -a,b,c)

## Setup the Jaeger and Prometheus source
TASK2 - DONE -  Expose Grafana to the internet and then setup Prometheus as a data source. screenshot after logging into Grafana - task2

## Create a Basic Dashboard
TASK3 - DONE - Create a dashboard in" Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
TASK4 - DONE - Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
SLI for Monthly uptime is a mesurement of uptime (as observed by a liveness prob fro example) divided by total time in a month to get percentage 
SLI for request response time is a mesurement of  average time per request or even maximum time per request with theshold filtering of some small number of edge case

## Creating SLI metrics.
TASK5 - It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
1. number of failed requests - to remove these from r/s time 
2. total number of requests - to caclulate percentage
3. time for request/response - to calculate r/s average time
4. service uptime in percentage of timeframe (day,months etc)
5. system load - memory/cpu usage



## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
