Data = Normalized, Loss = Binary Cross Entropy, Activation = Softmax, Batch Size = 32, Epochs = 50, Learning Rate = 0.1

|                                      | Accuracy | Loss   |
| ------------------------------------ | -------- | ------ |
| **Single Layer** **(10)**            | 0.9248   | 0.0448 |
| **2 Layers (Outer = 10, Middle 5**)  | 0.7553   | 0.1269 |
| **2 Layers (Outer = 10, Middle 3**)  | 0.5605   | 0.2003 |
| **2 Layers (Outer = 10, Middle 10**) | 0.7478   | 0.1293 |

Data = Normalized, Loss = MSLE, Activation = ReLU, Batch Size = 32, Epochs = 50, Learning Rate = 0.1

|                                      | Accuracy | Loss   |
| ------------------------------------ | -------- | ------ |
| **Single Layer (10)**                | 0.9176   | 0.0081 |
| **2 Layers (Outer = 10, Middle 5)**  | 0.7411   | 0.0163 |
| **2 Layers (Outer = 10, Middle 3)**  | 0.6656   | 0.0235 |
| **2 Layers (Outer = 10, Middle 10)** | 0.8576   | 0.0099 |

