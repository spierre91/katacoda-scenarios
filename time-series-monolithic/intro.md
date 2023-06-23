Time series analysis workflows are made up of several distinct steps.
These include data exploration through summary statistics, data visualizations, and forward looking time series forecasts.
Very often, these tasks are completed using a monolithic and tightly coupled code base. This makes maintaining code used for time
series forecasting tasks harder to read, maintain and scale. Refactoring is the process of rewriting code readability, maintainability,
and scalability are enhanced while keeps functionality. One common way to refactor code is using functions and classes.

Choosing between a monolithic codebase and something more modular depends on a variety of factors. These include the complexity of the tasks being performed, the size of the code base, the need to reuse parts of the code, collaboration efforts, and more. Operations that complex, repeatedly used, and shared are better refactored using functions and classes.
If a monolothic code base is going to be used by a small group of people and the operations are simple, it is probably fine to stick to a monolithic codebase. Further, even if the operations are simple, if there is a great deal of duplicate code in your monolithic codebase, it is advisable
to perform refactoring.

Using functions to refactor code involves breaking code up into small self-contained functions. Further, it sis common to define this functions
using the single responsibility principle (SRP). SRP simply states that function and classes should be responsible for a single task.
This enhances the testability, readability and reusability of the code. For example, if you have a monolithic code base that reads in time series data,
prepares it for training a forecasting model, trains the model, and validates performance, each of these steps can be incorporated into single
responsibility functions.

You can further improve readability and reusability by refactoring code using python classes. This involves defining classes that encapsulate similar data and operations. For example, we can split a time series analysis workflow into exploratory data analysis, data preparation, model training, and model evaluations. Depending on the complexity and code base size, it may be useful to split each of these operations into single responsibility classes. The methods defined in the single repsonsibility classes should also, ideally, be single responbility functions.

In these labs, you will learning how to transform monolithic time series analysis code into more modular units that are easier to read, share, scale and test. We will start by specifying the logic for each step in our time series analysis in a monolithic version of our code. We will then see how we can remove duplicated logic, and enforce SRP to break the monolithic code into well-define functions. Finally, we will see how we can encapsulate similar operations for EDA, data prep, model building, and model evaluation into single responsibility classes.
The target audience for these labs are python developers, data scientists, machine learning engineers, data analysts, software engineers and students of computer science learning python. Having some experience with coding and python and a basic knowledge of data analysis in python would ensure that students get the most from the labs.
