function gcd(a,b){
    let f = a;
    let s = b;
    while(s!=0){
        let temp = f%s;
        f = s;
        s = temp;
    }
    return f;
}

function lcm(a,b){
    return (a*b)/gcd(a,b);
}

export { gcd, lcm }