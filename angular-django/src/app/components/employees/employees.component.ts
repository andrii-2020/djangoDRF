import {Component, OnInit} from '@angular/core';
import {IEmployees} from '../../interfaces/employees';
import {OfficeService} from '../../services/office-service';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.css']
})
export class EmployeesComponent implements OnInit {
  employees: IEmployees[];
  constructor(private officeService: OfficeService) {
  }

  ngOnInit(): void {
    this.officeService.getEmployees().subscribe(val => {
      this.employees = val;

    });
  }

   deleteEmp(id: number): void {
     this.officeService.deleteEmployees(id).subscribe(() => this.ngOnInit());
  }
}
