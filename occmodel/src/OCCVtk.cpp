#include "OCCModel.h"


PyObject* c_shapeToActor(OCCBase* occShape)
{

    // Initialize aShape variable: e.g. load it from BREP file
    IVtkOCC_Shape::Handle aShapeImpl = new IVtkOCC_Shape(occShape->getShape());

    vtkSmartPointer<IVtkTools_ShapeDataSource> DS = vtkSmartPointer<IVtkTools_ShapeDataSource>::New();
    DS->SetShape(aShapeImpl);

    vtkSmartPointer<vtkPolyDataMapper> Mapper = vtkSmartPointer<vtkPolyDataMapper>::New();
    Mapper->SetInputConnection(DS->GetOutputPort());
    vtkSmartPointer<vtkActor> Actor = vtkSmartPointer<vtkActor>::New();
    Actor->SetMapper(Mapper);

    return vtkPythonUtil::GetObjectFromPointer(Actor);
}