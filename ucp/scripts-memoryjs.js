function dec2bin(num,bits)
{
  var i, binRep, neg;

  neg = false;
  binRep = "";

  if (num < 0)
  {
    num = -num;
    neg = true;
  }

  for(i=0; i<bits; i++)
  {
    if (num % 2 == 0)
      binRep = "0" + binRep;
    else
      binRep = "1" + binRep;

    num = Math.floor(num / 2);
  }

  if (neg)
    binRep = twosComp(binRep);

  return(binRep);
}

function bin2dec(num, isSigned)
{
  var theVal, i, neg;

  neg = false;
  theVal = 0;

  if (num.charAt(0) == '1' && isSigned)
  {
    neg = true;
    num = twosComp(num);
  }

  for (i=0; i<num.length; i++)
  {
     theVal = theVal + Math.pow(2,i)*(parseInt(num.charAt(num.length-i-1)));
  }

  if (neg)
    theVal = -theVal;

  return theVal;
}

function twosComp(binNum)
{
  var flipEM, i, twosCVal;

  twosCVal = "";
  flipEM = false;

  for (i=binNum.length-1; i>=0; i--)
  {
    if (flipEM)
    twosCVal = ((parseInt(binNum.charAt(i)) + 1) % 2) +
                 twosCVal;
    else
    {
      twosCVal = binNum.charAt(i) + twosCVal;
      flipEM = (binNum.charAt(i) == '1')
    }
  }
        
  return twosCVal;
}

function getInstruction(theOpcode)
{
  var theOP;

  theOP = theOpcode.substring(0,9);
  
  if      (theOP == "100000010")
    return "LOAD R" + 
           getNumber(theOpcode.substring(9,11),2,10,2) + " " +
           getNumber(theOpcode.substring(11,16),2,10,5);
  else if (theOP == "100000100")
    return "STORE " + 
           getNumber(theOpcode.substring(11,16),2,10,5) + " R" +
           getNumber(theOpcode.substring(9,11),2,10,2);
  else if (theOP == "100100010")
    return "MOVE R" +
           getNumber(theOpcode.substring(12,14),2,10,2) + " R" +
           getNumber(theOpcode.substring(14,16),2,10,2);

  else if (theOP == "101000010")
    return "ADD" + getRRR(theOpcode);
  else if (theOP == "101000100")
    return "SUB" + getRRR(theOpcode);
  else if (theOP == "101000110")
    return "AND" + getRRR(theOpcode);
  else if (theOP == "101001000")
    return "OR" + getRRR(theOpcode);

  else if (theOP == "000000010")
    return "BRANCH " + 
           getNumber(theOpcode.substring(11,16),2,10,5);
  else if (theOP == "000000100")
    return "BZERO " +
           getNumber(theOpcode.substring(11,16),2,10,5);
  else if (theOP == "000000110")
    return "BNEG " + 
           getNumber(theOpcode.substring(11,16),2,10,5);

  else if (theOpcode == "0000000000000000")
    return "NOP";
  else if (theOpcode == "1111111111111111")
    return "HALT";
  else 
    return "ILLEGAL OPCODE";
}

function getRRR(theOpcode)
{
  return " R" + getNumber(theOpcode.substring(10,12),2,10,2) + 
         " R" + getNumber(theOpcode.substring(12,14),2,10,2) + 
         " R" + getNumber(theOpcode.substring(14,16),2,10,2);
}

function getOpcode(theNum)
{
  var key;

  key = theNum.substring(0,2);

  if      (key == "LO")
    return "100000010" + 
           getNumber(theNum.substring(6,7),10,2,2) +
           getNumber(theNum.substring(8,theNum.length),10,2,5);
  else if (key == "ST")
    return "100000100" +
           getNumber(theNum.substring(theNum.length-1,theNum.length),10,2,2) +
           getNumber(theNum.substring(6,theNum.length-3),10,2,5);

  else if (key == "MO")
    return "100100010000" +
           getNumber(theNum.substring(6,7),10,2,2) +
           getNumber(theNum.substring(9,10),10,2,2);

  else if (key == "AD")
    return "1010000100" + 
           getNumber(theNum.substring(5,6),10,2,2) +
           getNumber(theNum.substring(8,9),10,2,2) +
           getNumber(theNum.substring(11,12),10,2,2);
  else if (key == "SU")
    return "1010001000" + 
           getNumber(theNum.substring(5,6),10,2,2) +
           getNumber(theNum.substring(8,9),10,2,2) +
           getNumber(theNum.substring(11,12),10,2,2);
  else if (key == "AN")
    return "1010001100" + 
           getNumber(theNum.substring(5,6),10,2,2) +
           getNumber(theNum.substring(8,9),10,2,2) +
           getNumber(theNum.substring(11,12),10,2,2);
  else if (key == "OR")
    return "1010010000" + 
           getNumber(theNum.substring(4,5),10,2,2) +
           getNumber(theNum.substring(7,8),10,2,2) +
           getNumber(theNum.substring(10,11),10,2,2);
  else if (key == "BR")
    return "00000001000" +
           getNumber(theNum.substring(7,theNum.length),10,2,5);
  else if (key == "BZ")
    return "00000010000" +
           getNumber(theNum.substring(6,theNum.length),10,2,5);
  else if (key == "BN")
    return "00000011000" +
           getNumber(theNum.substring(5,theNum.length),10,2,5);
  else if (key == "NO")
    return "0000000000000000";
  else if (key == "HA")
    return "1111111111111111";
  else
    return "ILLEGAL INSTRUCTION";
}

function getNumber(theNum,fromBase,toBase,bits)
{
  var base2Val, isSigned;

  isSigned=false;

  if (toBase == -10)
  {
    toBase = 10;
    isSigned = true;
  }

  if (fromBase == 10 || fromBase == -10)
    base2Val = dec2bin(theNum,bits);
  else if (fromBase == -1)
    base2Val = getOpcode(theNum);
  else if (fromBase == 2)
    base2Val = theNum;

  if (toBase == 10)
    return bin2dec(base2Val,isSigned);
  else if (toBase == -1)
    return getInstruction(base2Val);
  else if (toBase == 2)
    return base2Val;
  else
    return "BAD BASE CONVERSION";
}

function validInstruction(theInst)
{
  return validLOAD(theInst) || validSTORE(theInst) || 
         validMOVE(theInst) || validArithOrLogic(theInst) ||
         validBRANCH(theInst) || validHALTorNOP(theInst);
} 

function isValidRegister(theReg)
{
  return (theReg.charAt(0) == 'R' &&
          parseInt(theReg.substring(1,theReg.length)) >= 0 &&
          parseInt(theReg.substring(1,theReg.length)) <= 3);
}

function isValidMemory(theMem)
{
  return (parseInt(theMem) >= 0 &&
          parseInt(theMem) <= 31);
}

function validLOAD(theInst)
{
  var parts;
  parts = theInst.split(" ");
  
  return (parts[0] == "LOAD" &&
          isValidRegister(parts[1]) &&
          isValidMemory(parts[2]) &&
          parts.length == 3);
}

function validSTORE(theInst)
{
  var parts;
  parts = theInst.split(" ");

  return (parts[0] == "STORE" &&
          isValidMemory(parts[1]) &&
          isValidRegister(parts[2]) &&
          parts.length == 3);
}

function validMOVE(theInst)
{
  var parts;
  parts = theInst.split(" ");

  return (parts[0] == "MOVE" &&
          isValidRegister(parts[1]) &&
          isValidRegister(parts[2]) &&
          parts.length == 3);
}

function validArithOrLogic(theInst)
{
  var parts;
  parts = theInst.split(" ");

  return ((parts[0] == "ADD" || parts[0] == "SUB" || parts[0] == "AND" || parts[0] == "OR") &&
          isValidRegister(parts[1]) &&
          isValidRegister(parts[2]) &&
          isValidRegister(parts[3]) &&
          parts.length == 4);
}

function validBRANCH(theInst)
{
  var parts;
  parts = theInst.split(" ");

  return ((parts[0] == "BRANCH" || parts[0] == "BZERO" || parts[0] == "BNEG") &&
          isValidMemory(parts[1]) &&
          parts.length == 2);
}

function validHALTorNOP(theInst)
{  
  var parts;
  parts = theInst.split(" ");

  return ((parts[0] == "HALT" || parts[0] == "NOP") &&
          parts.length == 1);
}