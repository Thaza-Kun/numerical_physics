// main.rs

struct Answer {
    value: f64,
    uncertainty: f64
}

type Function = fn(&f64) -> Result<f64, String>;

fn foo(point: &f64) -> Result<f64, String> {
    Ok(point.powi(2) - 4.)
}

fn deriv_foo(point: &f64) -> Result<f64, String> {
    if &2.*point == 0. {
        return Err(format!("Illegal value on deriv_func: {}", point));
    }
    Ok(&2.*point)
}

fn root_by_newton(func: Function, deriv_func: Function, initial: f64, tolerance: Option<f64>, limit: Option<i64>) -> Result<Answer, String> {
    let tolerance = tolerance.unwrap_or(1e-6);
    let limit = limit.unwrap_or(100);
    let mut point = initial;

    let mut run = 1;
    loop {
        let intercept = point - {func(&point).unwrap()/deriv_func(&point).unwrap()};
        let interval = {point - intercept}.abs();
        point = intercept;
        if interval < tolerance {
            break Ok(Answer{value: point, uncertainty: interval/2.})
        }
        run += 1;
        if run == limit {break Err(format!("Loop has run {} times and no answer was found. Consider using other initial guess.", limit))}

    }
}

fn main() {
    let answer = root_by_newton(foo, deriv_foo, 0., None, None).expect("Answer cannot be computed");
    println!("The function has root at {} +_ {}", answer.value, answer.uncertainty)
    
}
