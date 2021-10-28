// Generated by gencpp from file multi_map_server/VerticalOccupancyGridList.msg
// DO NOT EDIT!


#ifndef MULTI_MAP_SERVER_MESSAGE_VERTICALOCCUPANCYGRIDLIST_H
#define MULTI_MAP_SERVER_MESSAGE_VERTICALOCCUPANCYGRIDLIST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace multi_map_server
{
template <class ContainerAllocator>
struct VerticalOccupancyGridList_
{
  typedef VerticalOccupancyGridList_<ContainerAllocator> Type;

  VerticalOccupancyGridList_()
    : x(0.0)
    , y(0.0)
    , upper()
    , lower()
    , mass()  {
    }
  VerticalOccupancyGridList_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , upper(_alloc)
    , lower(_alloc)
    , mass(_alloc)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _upper_type;
  _upper_type upper;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _lower_type;
  _lower_type lower;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _mass_type;
  _mass_type mass;





  typedef boost::shared_ptr< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> const> ConstPtr;

}; // struct VerticalOccupancyGridList_

typedef ::multi_map_server::VerticalOccupancyGridList_<std::allocator<void> > VerticalOccupancyGridList;

typedef boost::shared_ptr< ::multi_map_server::VerticalOccupancyGridList > VerticalOccupancyGridListPtr;
typedef boost::shared_ptr< ::multi_map_server::VerticalOccupancyGridList const> VerticalOccupancyGridListConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator1> & lhs, const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.upper == rhs.upper &&
    lhs.lower == rhs.lower &&
    lhs.mass == rhs.mass;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator1> & lhs, const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace multi_map_server

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7ef85cc95b82747f51eb01a16bd7c795";
  }

  static const char* value(const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7ef85cc95b82747fULL;
  static const uint64_t static_value2 = 0x51eb01a16bd7c795ULL;
};

template<class ContainerAllocator>
struct DataType< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "multi_map_server/VerticalOccupancyGridList";
  }

  static const char* value(const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"int32[] upper\n"
"int32[] lower\n"
"int32[] mass\n"
"\n"
;
  }

  static const char* value(const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.upper);
      stream.next(m.lower);
      stream.next(m.mass);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VerticalOccupancyGridList_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::multi_map_server::VerticalOccupancyGridList_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "upper[]" << std::endl;
    for (size_t i = 0; i < v.upper.size(); ++i)
    {
      s << indent << "  upper[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.upper[i]);
    }
    s << indent << "lower[]" << std::endl;
    for (size_t i = 0; i < v.lower.size(); ++i)
    {
      s << indent << "  lower[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.lower[i]);
    }
    s << indent << "mass[]" << std::endl;
    for (size_t i = 0; i < v.mass.size(); ++i)
    {
      s << indent << "  mass[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.mass[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MULTI_MAP_SERVER_MESSAGE_VERTICALOCCUPANCYGRIDLIST_H
