# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution:
> 
profitable path: tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB  
swap, tokenB->tokenA, AmountIn =  5                  , AmountOut = 5.655321988655322  
swap, tokenA->tokenC, AmountIn =  5.655321988655322  , AmountOut = 2.37213893638309  
swap, tokenC->tokenE, AmountIn =  2.37213893638309   , AmountOut = 1.5301371369636172  
swap, tokenE->tokenD, AmountIn =  1.5301371369636172 , AmountOut = 3.450741448619709  
swap, tokenD->tokenC, AmountIn =  3.450741448619709  , AmountOut = 6.68452557957259  
swap, tokenC->tokenB, AmountIn =  6.68452557957259   , AmountOut = 22.497221806974142  
tokenB balance = 22.497221806974142  
## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution:
> 
滑點是指在進行交易時，由於交易對的流動性不足或市場波動，導致交易成交價格與預期價格之間的差異。Uniswap V2通過採用恆定乘積市場製造者（Constant Product Market Maker）的模型來解決這個問題。這個模型通過將兩個資產的數量的乘積保持不變來確保流動性。舉個例子，假設有一個函數 calculateOutputPrice 用於計算購買某個資產所需的價格，Uniswap V2 通過以下方式來處理滑點：
> 
function calculateOutputPrice(uint256 inputAmount, uint256 inputReserve, uint256 outputReserve) external pure returns (uint256) {
require(inputReserve > 0 && outputReserve > 0, "Reserves must be greater than 0");  
uint256 inputAmountWithFee = inputAmount.mul(997);  
uint256 numerator = inputAmountWithFee.mul(outputReserve);  
uint256 denominator = inputReserve.mul(1000).add(inputAmountWithFee);  
return numerator / denominator;  
}

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution:
> 
在UniswapV2Pair合約的mint函數中，減去最小流動性的設計是為了防止恶意行为和保護流動性提供者。這麼做可以確保在流動池中添加的資產足夠多，從而確保流動性池的穩定性和安全性。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution:
> 
在UniswapV2Pair合約的鑄造函數中，當存入代幣時，使用的特定公式是為了確保流動性提供者不會因爲價格變動而受到不公平的損失。這個公式通常涉及到計算存入的代幣數量和流動性份額之間的比率，以確保按照公平的價格將流動性添加到池中。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution:
> 
夾擊攻擊是一種在去中心化交易所中進行的交易攻擊。攻擊者在發現一個正在進行的交易後，快速進行兩個相反方向的交易，將交易價格推動到不利於原始交易方的方向，從而從中獲利。當你發起交易時，夾擊攻擊可能會導致你得到的價格不符合預期，並可能導致損失。為了減少夾擊攻擊的風險，可以採取一些措施，例如減少交易量、使用更低的滑點交易對等。

