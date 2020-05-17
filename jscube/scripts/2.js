function setMark(){
    cube.front.northWest["front"].element.getElementsByClassName("underline")[0].innerText = "F0"
    cube.front.north["front"].element.getElementsByClassName("underline")[0].innerText =     "F1"
    cube.front.northEast["front"].element.getElementsByClassName("underline")[0].innerText = "F2"
    cube.front.west["front"].element.getElementsByClassName("underline")[0].innerText =      "F3"
    cube.front.origin["front"].element.getElementsByClassName("underline")[0].innerText =    "F4"
    cube.front.east["front"].element.getElementsByClassName("underline")[0].innerText =      "F5"
    cube.front.southWest["front"].element.getElementsByClassName("underline")[0].innerText = "F6"
    cube.front.south["front"].element.getElementsByClassName("underline")[0].innerText =     "F7"
    cube.front.southEast["front"].element.getElementsByClassName("underline")[0].innerText = "F8"

    cube.right.northWest["right"].element.getElementsByClassName("underline")[0].innerText = "R0"
    cube.right.north["right"].element.getElementsByClassName("underline")[0].innerText =     "R1"
    cube.right.northEast["right"].element.getElementsByClassName("underline")[0].innerText = "R2"
    cube.right.west["right"].element.getElementsByClassName("underline")[0].innerText =      "R3"
    cube.right.origin["right"].element.getElementsByClassName("underline")[0].innerText =    "R4"
    cube.right.east["right"].element.getElementsByClassName("underline")[0].innerText =      "R5"
    cube.right.southWest["right"].element.getElementsByClassName("underline")[0].innerText = "R6"
    cube.right.south["right"].element.getElementsByClassName("underline")[0].innerText =     "R7"
    cube.right.southEast["right"].element.getElementsByClassName("underline")[0].innerText = "R8"

    cube.left.northWest["left"].element.getElementsByClassName("underline")[0].innerText = "L6"
    cube.left.north["left"].element.getElementsByClassName("underline")[0].innerText =     "L3"
    cube.left.northEast["left"].element.getElementsByClassName("underline")[0].innerText = "L0"
    cube.left.west["left"].element.getElementsByClassName("underline")[0].innerText =      "L7"
    cube.left.origin["left"].element.getElementsByClassName("underline")[0].innerText =    "L4"
    cube.left.east["left"].element.getElementsByClassName("underline")[0].innerText =      "L1"
    cube.left.southWest["left"].element.getElementsByClassName("underline")[0].innerText = "L8"
    cube.left.south["left"].element.getElementsByClassName("underline")[0].innerText =     "L5"
    cube.left.southEast["left"].element.getElementsByClassName("underline")[0].innerText = "L2"

    cube.up.northWest["up"].element.getElementsByClassName("underline")[0].innerText = "U0"
    cube.up.north["up"].element.getElementsByClassName("underline")[0].innerText =     "U1"
    cube.up.northEast["up"].element.getElementsByClassName("underline")[0].innerText = "U2"
    cube.up.west["up"].element.getElementsByClassName("underline")[0].innerText =      "U3"
    cube.up.origin["up"].element.getElementsByClassName("underline")[0].innerText =    "U4"
    cube.up.east["up"].element.getElementsByClassName("underline")[0].innerText =      "U5"
    cube.up.southWest["up"].element.getElementsByClassName("underline")[0].innerText = "U6"
    cube.up.south["up"].element.getElementsByClassName("underline")[0].innerText =     "U7"
    cube.up.southEast["up"].element.getElementsByClassName("underline")[0].innerText = "U8"

    cube.down.northWest["down"].element.getElementsByClassName("underline")[0].innerText = "D2"
    cube.down.north["down"].element.getElementsByClassName("underline")[0].innerText =     "D5"
    cube.down.northEast["down"].element.getElementsByClassName("underline")[0].innerText = "D8"
    cube.down.west["down"].element.getElementsByClassName("underline")[0].innerText =      "D1"
    cube.down.origin["down"].element.getElementsByClassName("underline")[0].innerText =    "D4"
    cube.down.east["down"].element.getElementsByClassName("underline")[0].innerText =      "D7"
    cube.down.southWest["down"].element.getElementsByClassName("underline")[0].innerText = "D0"
    cube.down.south["down"].element.getElementsByClassName("underline")[0].innerText =     "D3"
    cube.down.southEast["down"].element.getElementsByClassName("underline")[0].innerText = "D6"

    cube.back.northWest["back"].element.getElementsByClassName("underline")[0].innerText = "B6"
    cube.back.north["back"].element.getElementsByClassName("underline")[0].innerText =     "B3"
    cube.back.northEast["back"].element.getElementsByClassName("underline")[0].innerText = "B0"
    cube.back.west["back"].element.getElementsByClassName("underline")[0].innerText =      "B7"
    cube.back.origin["back"].element.getElementsByClassName("underline")[0].innerText =    "B4"
    cube.back.east["back"].element.getElementsByClassName("underline")[0].innerText =      "B1"
    cube.back.southWest["back"].element.getElementsByClassName("underline")[0].innerText = "B8"
    cube.back.south["back"].element.getElementsByClassName("underline")[0].innerText =     "B5"
    cube.back.southEast["back"].element.getElementsByClassName("underline")[0].innerText = "B2"
}


function getMark(){
    f0 = cube.front.northWest["front"].element.getElementsByClassName("underline")[0].innerText 
    f1 = cube.front.north["front"].element.getElementsByClassName("underline")[0].innerText 
    f2 = cube.front.northEast["front"].element.getElementsByClassName("underline")[0].innerText 
    f3 = cube.front.west["front"].element.getElementsByClassName("underline")[0].innerText 
    f4 = cube.front.origin["front"].element.getElementsByClassName("underline")[0].innerText 
    f5 = cube.front.east["front"].element.getElementsByClassName("underline")[0].innerText 
    f6 = cube.front.southWest["front"].element.getElementsByClassName("underline")[0].innerText 
    f7 = cube.front.south["front"].element.getElementsByClassName("underline")[0].innerText 
    f8 = cube.front.southEast["front"].element.getElementsByClassName("underline")[0].innerText 

    r0 = cube.right.northWest["right"].element.getElementsByClassName("underline")[0].innerText 
    r1 = cube.right.north["right"].element.getElementsByClassName("underline")[0].innerText 
    r2 = cube.right.northEast["right"].element.getElementsByClassName("underline")[0].innerText 
    r3 = cube.right.west["right"].element.getElementsByClassName("underline")[0].innerText 
    r4 = cube.right.origin["right"].element.getElementsByClassName("underline")[0].innerText 
    r5 = cube.right.east["right"].element.getElementsByClassName("underline")[0].innerText 
    r6 = cube.right.southWest["right"].element.getElementsByClassName("underline")[0].innerText 
    r7 = cube.right.south["right"].element.getElementsByClassName("underline")[0].innerText 
    r8 = cube.right.southEast["right"].element.getElementsByClassName("underline")[0].innerText 

    l6 = cube.left.northWest["left"].element.getElementsByClassName("underline")[0].innerText 
    l3 = cube.left.north["left"].element.getElementsByClassName("underline")[0].innerText 
    l0 = cube.left.northEast["left"].element.getElementsByClassName("underline")[0].innerText 
    l7 = cube.left.west["left"].element.getElementsByClassName("underline")[0].innerText 
    l4 = cube.left.origin["left"].element.getElementsByClassName("underline")[0].innerText 
    l1 = cube.left.east["left"].element.getElementsByClassName("underline")[0].innerText 
    l8 = cube.left.southWest["left"].element.getElementsByClassName("underline")[0].innerText 
    l5 = cube.left.south["left"].element.getElementsByClassName("underline")[0].innerText 
    l2 = cube.left.southEast["left"].element.getElementsByClassName("underline")[0].innerText 

    u0 = cube.up.northWest["up"].element.getElementsByClassName("underline")[0].innerText 
    u1 = cube.up.north["up"].element.getElementsByClassName("underline")[0].innerText 
    u2 = cube.up.northEast["up"].element.getElementsByClassName("underline")[0].innerText 
    u3 = cube.up.west["up"].element.getElementsByClassName("underline")[0].innerText 
    u4 = cube.up.origin["up"].element.getElementsByClassName("underline")[0].innerText 
    u5 = cube.up.east["up"].element.getElementsByClassName("underline")[0].innerText 
    u6 = cube.up.southWest["up"].element.getElementsByClassName("underline")[0].innerText 
    u7 = cube.up.south["up"].element.getElementsByClassName("underline")[0].innerText 
    u8 = cube.up.southEast["up"].element.getElementsByClassName("underline")[0].innerText 

    d2 = cube.down.northWest["down"].element.getElementsByClassName("underline")[0].innerText 
    d5 = cube.down.north["down"].element.getElementsByClassName("underline")[0].innerText 
    d8 = cube.down.northEast["down"].element.getElementsByClassName("underline")[0].innerText 
    d1 = cube.down.west["down"].element.getElementsByClassName("underline")[0].innerText 
    d4 = cube.down.origin["down"].element.getElementsByClassName("underline")[0].innerText 
    d7 = cube.down.east["down"].element.getElementsByClassName("underline")[0].innerText 
    d0 = cube.down.southWest["down"].element.getElementsByClassName("underline")[0].innerText 
    d3 = cube.down.south["down"].element.getElementsByClassName("underline")[0].innerText 
    d6 = cube.down.southEast["down"].element.getElementsByClassName("underline")[0].innerText 

    b6 = cube.back.northWest["back"].element.getElementsByClassName("underline")[0].innerText 
    b3 = cube.back.north["back"].element.getElementsByClassName("underline")[0].innerText 
    b0 = cube.back.northEast["back"].element.getElementsByClassName("underline")[0].innerText 
    b7 = cube.back.west["back"].element.getElementsByClassName("underline")[0].innerText 
    b4 = cube.back.origin["back"].element.getElementsByClassName("underline")[0].innerText 
    b1 = cube.back.east["back"].element.getElementsByClassName("underline")[0].innerText 
    b8 = cube.back.southWest["back"].element.getElementsByClassName("underline")[0].innerText 
    b5 = cube.back.south["back"].element.getElementsByClassName("underline")[0].innerText 
    b2 = cube.back.southEast["back"].element.getElementsByClassName("underline")[0].innerText 

    console.log(
                "[['" + u0 + "', '" + u1 + "', '" + u2 + "'],",
                "['" + u3 + "', '" + u4 + "', '" + u5 + "'],",
                "['" + u6 + "', '" + u7 + "', '" + u8 + "'],",
                "['" + d0 + "', '" + d1 + "', '" + d2 + "'],",
                "['" + d3 + "', '" + d4 + "', '" + d5 + "'],",
                "['" + d6 + "', '" + d7 + "', '" + d8 + "'],",
                "['" + l0 + "', '" + l1 + "', '" + l2 + "'],",
                "['" + l3 + "', '" + l4 + "', '" + l5 + "'],",
                "['" + l6 + "', '" + l7 + "', '" + l8 + "'],",
                "['" + r0 + "', '" + r1 + "', '" + r2 + "'],",
                "['" + r3 + "', '" + r4 + "', '" + r5 + "'],",
                "['" + r6 + "', '" + r7 + "', '" + r8 + "'],",
                "['" + f0 + "', '" + f1 + "', '" + f2 + "'],",
                "['" + f3 + "', '" + f4 + "', '" + f5 + "'],",
                "['" + f6 + "', '" + f7 + "', '" + f8 + "'],",
                "['" + b0 + "', '" + b1 + "', '" + b2 + "'],",
                "['" + b3 + "', '" + b4 + "', '" + b5 + "'],",
                "['" + b6 + "', '" + b7 + "', '" + b8 + "']]"
    )
    console.log(
                "['" + u0 + "', '" + u1 + "', '" + u2 + "',",
                "'" + u3 + "', '" + u4 + "', '" + u5 + "',",
                "'" + u6 + "', '" + u7 + "', '" + u8 + "',",
                "'" + d0 + "', '" + d1 + "', '" + d2 + "',",
                "'" + d3 + "', '" + d4 + "', '" + d5 + "',",
                "'" + d6 + "', '" + d7 + "', '" + d8 + "',",
                "'" + l0 + "', '" + l1 + "', '" + l2 + "',",
                "'" + l3 + "', '" + l4 + "', '" + l5 + "',",
                "'" + l6 + "', '" + l7 + "', '" + l8 + "',",
                "'" + r0 + "', '" + r1 + "', '" + r2 + "',",
                "'" + r3 + "', '" + r4 + "', '" + r5 + "',",
                "'" + r6 + "', '" + r7 + "', '" + r8 + "',",
                "'" + f0 + "', '" + f1 + "', '" + f2 + "',",
                "'" + f3 + "', '" + f4 + "', '" + f5 + "',",
                "'" + f6 + "', '" + f7 + "', '" + f8 + "',",
                "'" + b0 + "', '" + b1 + "', '" + b2 + "',",
                "'" + b3 + "', '" + b4 + "', '" + b5 + "',",
                "'" + b6 + "', '" + b7 + "', '" + b8 + "']"
    )
}

function r(){
    undoToZero()
}


function e(actions){
    cube.twistDuration = 0
    cube.twist(actions)
}

function inputtwist(){
  if(event.keyCode==13){
    var x=  document.getElementById("textbox")
    e(x.value)
  }
}
