use std::fmt::Error;

// main.rs
// Root by bisection
fn main() {
    let answer = root_by_bisection(func, 0., 6., None).expect("Answer cannot be computed");
    print!("The function has root at {} +_ {}", answer.value, answer.uncertainty)
}

type Function = fn(&f64) -> Result<f64, String>;

/// An arbitrary function that we want to find the root of
fn func(point: &f64) -> Result<f64, String> {
    // Use this if there is an illegal value
    // if point == &0. {
    //     return Err(format!("Value {} is illegal", point))
    // }

    Ok(point.powi(2) - 4.0)
}

struct PhysicalValue {
    value: f64,
    uncertainty: f64,
}

fn root_by_bisection(_func: Function, mut left: f64, mut right: f64, tolerance: Option<f64>) -> Result<PhysicalValue, Error> {
    let tolerance = tolerance.unwrap_or(1.0e-6);
    let mut interval: f64 = (right - left).abs();
    let mut midpoint: f64 = 0.; // To initialize the value
    
    loop {
        if interval < tolerance {break Ok(PhysicalValue{value: midpoint, uncertainty: interval})}
        midpoint = (left - right) / 2.;
        if _func(&left).unwrap()*_func(&midpoint).unwrap() < 0. {
            right = midpoint
        } else {
            left = midpoint
        }
        interval = (right - left).abs();
    }
}
