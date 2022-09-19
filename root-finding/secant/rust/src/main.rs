// main.rs

struct Answer {
    value: f64,
    uncertainty: f64
}

type Function = fn(&f64) -> Result<f64, String>;

fn foo(point: &f64) -> Result<f64, String> {
    Ok(point.powi(2) - 4.)
}

fn root_by_secant(func: Function, mut first: f64, mut second: f64, tolerance: Option<f64>, limit: Option<i64>) -> Result<Answer, String> {
    let tolerance = tolerance.unwrap_or(1e-6);
    let limit = limit.unwrap_or(100);
    
    let mut run = 1;
    loop {
        let slope = {
            let x_diff = &second - &first;
            let y_diff = func(&second).unwrap() - func(&first).unwrap();
            if x_diff == 0. {
                0.
            } else {
                y_diff/x_diff
            }
        };
        let y_intercept = func(&first).unwrap() - slope*first;
        let x_intercept = - y_intercept/slope;
        let interval = {first-x_intercept}.abs();
        if interval < {second-x_intercept}.abs() {
            second = first
        }
        first = x_intercept;
        if interval < tolerance {
            break Ok(Answer{value: x_intercept, uncertainty: interval/2.})
        } 
        run += 1;
        if run == limit {break Err(format!("Loop has run {} times and no answer was found. Consider using other initial guess.", limit))}

    }
}

fn main() {
    let answer = root_by_secant(foo, 0.,0.1, None, None).expect("Answer cannot be computed");
    println!("The function has root at {} +_ {}", answer.value, answer.uncertainty)
    
}
