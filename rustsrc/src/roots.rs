pub struct Answer{
    pub value: f64,
    pub uncertainty: f64,
}

pub fn bisection(
    func: fn(&f64) -> Result<f64, String>,
    mut left: f64,
    mut right: f64,
    tolerance: Option<f64>,
    limit: Option<i64>,
) -> Result<Answer, String> {
    let tolerance = tolerance.unwrap_or(1.0e-6);
    let limit = limit.unwrap_or(100);

    let mut interval: f64 = (right - left).abs();
    let mut midpoint: f64 = 0.; // To initialize the value

    let mut run: i64 = 1;
    loop {
        if interval < tolerance {
            break Ok(Answer {
                value: midpoint,
                uncertainty: interval / 2.,
            });
        }
        midpoint = (left - right) / 2.;
        if func(&left).unwrap() * func(&midpoint).unwrap() < 0. {
            right = midpoint
        } else {
            left = midpoint
        }
        interval = (right - left).abs();
        run += 1;
        if run == limit {
            break Err(format!(
                "Loop has run {} times and no answer was found. Consider using other intervals.",
                limit
            ));
        }
    }
}

pub fn newton(
    func: fn(&f64) -> Result<f64, String>,
    deriv_func: fn(&f64) -> Result<f64, String>,
    initial: f64,
    tolerance: Option<f64>,
    limit: Option<i64>,
) -> Result<Answer, String> {
    let tolerance = tolerance.unwrap_or(1e-6);
    let limit = limit.unwrap_or(100);
    let mut point = initial;

    let mut run = 1;
    loop {
        let intercept = point - { func(&point).unwrap() / deriv_func(&point).unwrap() };
        let interval = { point - intercept }.abs();
        point = intercept;
        if interval < tolerance {
            break Ok(Answer {
                value: point,
                uncertainty: interval / 2.,
            });
        }
        run += 1;
        if run == limit {
            break Err(format!("Loop has run {} times and no answer was found. Consider using other initial guess.", limit));
        }
    }
}


pub fn secant(
    func: fn(&f64) -> Result<f64, String>,
    mut first: f64,
    mut second: f64,
    tolerance: Option<f64>,
    limit: Option<i64>,
) -> Result<Answer, String> {
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
                y_diff / x_diff
            }
        };
        let y_intercept = func(&first).unwrap() - slope * first;
        let x_intercept = -y_intercept / slope;
        let interval = { first - x_intercept }.abs();
        if interval < { second - x_intercept }.abs() {
            second = first
        }
        first = x_intercept;
        if interval < tolerance {
            break Ok(Answer {
                value: x_intercept,
                uncertainty: interval / 2.,
            });
        }
        run += 1;
        if run == limit {
            break Err(format!("Loop has run {} times and no answer was found. Consider using other initial guess.", limit));
        }
    }
}
