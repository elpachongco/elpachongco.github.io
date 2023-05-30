---
layout: post
title:  "Code Snippets #1: What the heck is hardhat's console.log?"
date:   2022-07-19 20:40:26 +0800
categories: programming
---

I was tasked to create ethereum smart contracts in my previous job. 

the library most recommended by other developers to create 
smart contracts was `hardhat`. 

to create and debug the smart contracts, I developed them using
test-driven-development methods. The tests gave  me a way to print out
and inspect variables. 

just as I was done with the development I read somewhere that hardhat has a
`console.log()` utility. You import it with `import hardhat/console.sol` and
use it like JS's `console.log`. I wondered how it worked. Upon testing, it
seemed to only allow a maximum amount of parameters. 

so i decided to look at hardhat's internals and find out how they do it. 

the first step was to find the `console.log()` utility function.

this is their repository
https://github.com/NomicFoundation/hardhat

```bash
$ ls 
config  CONTRIBUTING.md  crates  docs  LICENSE  package.json  packages  README.md  scripts  yarn.lock
```

im not familliar with their file structure conventions. But I can guess that
the source code is not in `config/`, `docs/`, or `scipts/`. 

```bash
$ ls crates packages
crates:
rethnet_evm_napi

packages:
common                 hardhat-core       hardhat-foundry          hardhat-solhint  hardhat-truffle4  hardhat-waffle
eslint-plugin          hardhat-ethers     hardhat-network-helpers  hardhat-solpp    hardhat-truffle5  hardhat-web3
hardhat-chai-matchers  hardhat-etherscan  hardhat-shorthand        hardhat-toolbox  hardhat-vyper     hardhat-web3-legacy
```

i didn't know what `crates/` were so I also tried it.
anyway, `packages/` contains `hardhat-core/`. Inside it we'll find 
`console.sol`.

let's see the code.

```bash
$ cat packages/hardhat-core/console.log
```

link to it:
https://github.com/NomicFoundation/hardhat/blob/main/packages/hardhat-core/console.sol

opening it, we find 1513 lines of repetitive, possibly auto-generated code. 

here's an interesting part of the code: 

```bash
$ cat packages/hardhat-core/console.sol  -n | tail -n 30
1503
1504          function log(address p0, address p1, bool p2, string memory p3) internal view {
1505                  _sendLogPayload(abi.encodeWithSignature("log(address,address,bool,string)", p0, p1, p2, p3));
1506          }
1507
1508          function log(address p0, address p1, bool p2, bool p3) internal view {
1509                  _sendLogPayload(abi.encodeWithSignature("log(address,address,bool,bool)", p0, p1, p2, p3));
1510          }
1511
1512          function log(address p0, address p1, bool p2, address p3) internal view {
1513                  _sendLogPayload(abi.encodeWithSignature("log(address,address,bool,address)", p0, p1, p2, p3));
1514          }
1515
1516          function log(address p0, address p1, address p2, uint256 p3) internal view {
1517                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,uint256)", p0, p1, p2, p3));
1518          }
1519
1520          function log(address p0, address p1, address p2, string memory p3) internal view {
1521                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,string)", p0, p1, p2, p3));
1522          }
1523
1524          function log(address p0, address p1, address p2, bool p3) internal view {
1525                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,bool)", p0, p1, p2, p3));
1526          }
1527
1528          function log(address p0, address p1, address p2, address p3) internal view {
1529                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,address)", p0, p1, p2, p3));
1530          }
1531
1532  }
```

this looks fascinating to me. I'm less familiar with statically-typed
languages, so I don't know how common this method is. I'll explain why it
intrigues me.

most of the file consist of functions with the name `log`. In python or
probably any dynamically-typed languages, this would not work. For example, if `log()` is
called, The interpreter would not know which `log`, to use out of the many `log`s defined.

```bash
1524          function log(address p0, address p1, address p2, bool p3) internal view {
1525                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,bool)", p0, p1, p2, p3));
1526          }
1527
1528          function log(address p0, address p1, address p2, address p3) internal view {
1529                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,address)", p0, p1, p2, p3));
1530          }
```

in solidity, this is a completely valid use case. Although the function
names are the same, the compiler can determine which `log` to use by looking at
the data types of the arguments, and finding which `log` function has  the
correct parameter data types.

```bash
1524          function log(address p0, address p1, address p2, bool p3) internal view {
1528          function log(address p0, address p1, address p2, address p3) internal view {
```

For example, these two function definitions are almost the same, except the
fourth parmeter. Line `1524` handles `log` calls with specifically 4 parameters
with respective types: `address`,  `address` ,  `address`, and `bool`. 

Whereas Line `1528` handles `log` calls that pass exactly 4 address data types.

```bash
1524          function log(address p0, address p1, address p2, bool p3) internal view {
1525                  _sendLogPayload(abi.encodeWithSignature("log(address,address,address,bool)", p0, p1, p2, p3));
1526          }
```

This design means that only a fixed number of arguments can be accepted by hardhat's console.log.
Console.log will not work if it's supplied with arguments that are not pre-defined in `console.sol`.

I later found the script that generates this code. It's in
`hardhat/packages/hardhat-core/scripts/console-library-generator.js`.

The parameters `p0` to `p3`, are passed to
`abi.encodeWithSignature` which is then passed to `_sendLogPayload`.

```bash
$ cat packages/hardhat-core/console.log -n | head -n 14
 1  // SPDX-License-Identifier: MIT
 2  pragma solidity >= 0.4.22 <0.9.0;
 3
 4  library console {
 5          address constant CONSOLE_ADDRESS = address(0x000000000000000000636F6e736F6c652e6c6f67);
 6
 7          function _sendLogPayload(bytes memory payload) private view {
 8                  uint256 payloadLength = payload.length;
 9                  address consoleAddress = CONSOLE_ADDRESS;
10                  assembly {
11                          let payloadStart := add(payload, 32)
12                          let r := staticcall(gas(), consoleAddress, payloadStart, payloadLength, 0, 0)
13                  }
14          }
```

At first glance, I can deduce that Hardhat sends the messages from `console.log`
to a dedicated public address. It then scans the address for messages and
outputs any messages that are sent to it to the terminal.

So that's Hardhat's console.log. We looked at its internals and found
mysterious code that turned out to be a smart solution to the problem.  
