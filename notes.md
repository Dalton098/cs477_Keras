Normalizing the data provided the greatest increase in performance. It increased the accuracy by roughly 0.4 and decreased the loss as well.

Mean Squared Logarithmic Error Loss was the best loss function I found out of Mean Squared Error, Mean Absolute Error, Binary Cross-Entropy Loss, Hinge Loss, and Squared Hinge Loss.

For activations I found the softmax to be the best. Others I tried were tanh, sigmoid, and logistic.

Decreasing the batch size to something like 10 made the program take much more time and did not improve the performance that much. When I changed the batch size to 32 I seemed to get the best results.z

Increasing the epochs increased the the overall performance as well I settled on leaving epochs at 50

I tried changing the learning rate to 0.5 but this made the performance significantly worse. I adjusted the learning rate to 0.1 as it seemed to give the best results. The original 0.01 was still relatively close in comparison though but still performed worse on average.