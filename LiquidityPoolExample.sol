pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint amount) external returns (bool);
    function transfer(address to, uint amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint);
    function approve(address spender, uint amount) external returns (bool);
}

contract SimplifiedUniswapV2 {
    IERC20 public tokenA;
    IERC20 public tokenB;

    uint public reserveA;
    uint public reserveB;

    constructor(address _tokenA, address _tokenB) {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    // Add liquidity to the pool
    function addLiquidity(uint amountA, uint amountB) external {
        tokenA.transferFrom(msg.sender, address(this), amountA);
        tokenB.transferFrom(msg.sender, address(this), amountB);

        reserveA += amountA;
        reserveB += amountB;
    }

    // Swap tokenA for tokenB
    function swapAtoB(uint amountIn) external {
        uint amountOut = getAmountOut(amountIn, reserveA, reserveB);

        tokenA.transferFrom(msg.sender, address(this), amountIn);
        tokenB.transfer(msg.sender, amountOut);

        reserveA += amountIn;
        reserveB -= amountOut;
    }

    // Uniswap V2 CPMM pricing formula with 0.3% fee
    function getAmountOut(uint amountIn, uint reserveIn, uint reserveOut) public pure returns (uint) {
        uint amountInWithFee = amountIn * 997;
        uint numerator = amountInWithFee * reserveOut;
        uint denominator = reserveIn * 1000 + amountInWithFee;
        return numerator / denominator;
    }

    // Return current pool reserves
    function getReserves() external view returns (uint, uint) {
        return (reserveA, reserveB);
    }
}