import os

class Report:
    def __init__(self, array):
        self.array = array
        self.safe = False
    
    def check_safe(self):
        increasing = False 
        
        # Check if increasing or decreasing
        if self.array[0] < self.array[-1]:
            increasing = True
        elif self.array[0] > self.array[-1]:
            increasing = False
        else:
            return 
        
        # Check difference between each number
        for i in range(0, len(self.array) - 1):
            if increasing:
                if self.array[i+1] - self.array[i] < 1 or self.array[i+1] - self.array[i] > 3:
                    return
            else:
                if self.array[i+1] - self.array[i] > -1 or self.array[i+1] - self.array[i] < -3:
                    return
        
        # If no issues found, set safe to True     
        self.safe = True
        return
            
            
def load_reports_from_file(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split('\n')[0]
            array = list(map(int, line.split(' ')))
            reports.append(Report(array))
    return reports

# Example usage
if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    safe_count = 0
    reports = load_reports_from_file(input_file)
    for report in reports:
        report.check_safe()
        if report.safe:
            safe_count += 1
    print(safe_count, '/', len(reports), 'are safe')