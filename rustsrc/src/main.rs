mod roots;
fn main() {
    println!("Finding root of x^2 + 4");
    let answer = roots::bisection(foo, 0.0, 6.0, None, None).unwrap();
    println!("Bisection {} {}",answer.value, answer.uncertainty);
    let answer = roots::newton(foo, deriv_foo, 2., None, None).unwrap();
    println!("Newton {} {}",answer.value, answer.uncertainty);
    let answer = roots::secant(foo, 0.1, 3.0, None, None).unwrap();
    println!("Secant {} {}",answer.value, answer.uncertainty);
}

fn foo(point: f64) -> Result<f64, String> {
    Ok(point.powi(2) - 4.)
}

fn deriv_foo(point: f64) -> Result<f64, String> {
    Ok(2.*point)
}
