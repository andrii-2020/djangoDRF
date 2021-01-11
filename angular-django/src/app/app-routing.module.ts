import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {OfficesComponent} from './components/offices/offices.component';
import {ReactiveFormsModule} from '@angular/forms';
import {EmployeesComponent} from './components/employees/employees.component';




const routes: Routes = [
  {
    path: 'offices', component: OfficesComponent
  },
  {
    path: 'employees', component: EmployeesComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes), ReactiveFormsModule],
  declarations: [
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
